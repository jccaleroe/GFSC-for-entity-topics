import com.google.protobuf.ByteString;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import nvidia.inferenceserver.Api.InferRequestHeader;
import nvidia.inferenceserver.GRPCServiceGrpc;
import nvidia.inferenceserver.GrpcServiceProto;
import nvidia.inferenceserver.GrpcServiceProto.InferRequest;

public class MNISTClient {

    private static byte[] floatArrayToByteArray(float[] floats) {
        byte[] bytes = new byte[floats.length * 4];
        int aux = 0;
        for (int i = 0; i < bytes.length; i += 4) {
            int tmp = Float.floatToIntBits(floats[aux++]);
            bytes[i] = (byte) (tmp & 255);
            bytes[i + 1] = (byte) ((tmp >> 8) & 255);
            bytes[i + 2] = (byte) ((tmp >> 16) & 255);
            bytes[i + 3] = (byte) ((tmp >> 24) & 255);
        }
        return bytes;
    }

    private static void run() {

        InferRequest.Builder inferRequest = InferRequest.newBuilder();
        inferRequest.setModelName("mnist");
        inferRequest.setModelVersion(-1);
        int batchSize = 1;

        float[] input = new float[28 * 28];
        InferRequestHeader.Builder rhBuilder = InferRequestHeader.newBuilder();
        rhBuilder.setFlags(InferRequestHeader.Flag.FLAG_NONE_VALUE);

        InferRequestHeader.Input.Builder labelIdBuilder = InferRequestHeader.Input.newBuilder();
        labelIdBuilder.setName("flatten_input");

        InferRequestHeader.Output.Builder probabilitiesBuilder = InferRequestHeader.Output.newBuilder();
        probabilitiesBuilder.setName("dense_1");

        rhBuilder.addInput(labelIdBuilder.build());
        inferRequest.addRawInput(ByteString.copyFrom(floatArrayToByteArray(input)));

        rhBuilder.addOutput(probabilitiesBuilder.build());
        rhBuilder.setBatchSize(batchSize);
        inferRequest.setMetaData(rhBuilder.build());

        InferRequest request = inferRequest.build();
        System.out.println(inferRequest);

        final ManagedChannel channel = ManagedChannelBuilder.forTarget("localhost:8001").usePlaintext().build();

        GRPCServiceGrpc.GRPCServiceBlockingStub blockingStub = GRPCServiceGrpc.newBlockingStub(channel);
        GrpcServiceProto.InferResponse inferResponse = blockingStub.infer(request);
        System.out.println(inferResponse.getMetaData());
        System.out.println(inferResponse.getRequestStatus());

        byte[] bytes = inferResponse.getRawOutput(0).toByteArray();

        for (int i = 0; i < bytes.length; i += 4) {
            int asInt = (bytes[i] & 0xFF)
                    | ((bytes[i + 1] & 0xFF) << 8)
                    | ((bytes[i + 2] & 0xFF) << 16)
                    | ((bytes[i + 3] & 0xFF) << 24);
            System.out.print(Float.intBitsToFloat(asInt) + " ");
        }
        System.out.println();

        channel.shutdownNow();
    }

    public static void main(String[] args) {
        run();
    }
}

