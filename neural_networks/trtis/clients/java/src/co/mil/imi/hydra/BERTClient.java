package co.mil.imi.hydra;

import com.google.protobuf.ByteString;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.stub.StreamObserver;
import nvidia.inferenceserver.Api.InferRequestHeader;
import nvidia.inferenceserver.GRPCServiceGrpc;
import nvidia.inferenceserver.GrpcServiceProto;
import nvidia.inferenceserver.GrpcServiceProto.InferRequest;

public class BERTClient {

    private static byte[] intArrayToByteArray(int[] integers) {
        byte[] bytes = new byte[integers.length * 4];
        int aux = 0;
        for (int i = 0; i < bytes.length; i += 4) {
            bytes[i] = (byte) (integers[aux] & 255);
            bytes[i + 1] = (byte) ((integers[aux] >> 8) & 255);
            bytes[i + 2] = (byte) ((integers[aux] >> 16) & 255);
            bytes[i + 3] = (byte) ((integers[aux++] >> 24) & 255);
        }
        return bytes;
    }

    private static void byteArrayToFloatArray(byte[] bytes) {
        for (int i = 0; i < bytes.length; i += 4) {
            int asInt = (bytes[i] & 0xFF)
                    | ((bytes[i + 1] & 0xFF) << 8)
                    | ((bytes[i + 2] & 0xFF) << 16)
                    | ((bytes[i + 3] & 0xFF) << 24);
            System.out.print(Float.intBitsToFloat(asInt) + " ");
        }
        System.out.println();
    }

    private static void run() {
        InferRequest.Builder inferRequest = InferRequest.newBuilder();
        inferRequest.setModelName("bert");
        inferRequest.setModelVersion(-1);
        int batchSize = 1;

        int[] inputIds = {101, 7473, 2278, 2860, 1005, 1055, 2708, 4082, 2961, 1010, 3505, 14998, 1010, 1998, 4074, 5196, 1010, 1996, 2708, 3361, 2961, 1010, 2097, 3189, 3495, 2000, 2720, 2061, 1012, 102, 2783, 2708, 4082, 2961, 3505, 14998, 1998, 2177, 2708, 3361, 2961, 4074, 5196, 2097, 3189, 2000, 2061, 1012, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        int[] inputMask = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        int[] segmentIds = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        int[] labelId = {0};

        InferRequestHeader.Builder rhBuilder = InferRequestHeader.newBuilder();
        rhBuilder.setFlags(InferRequestHeader.Flag.FLAG_NONE_VALUE);

        InferRequestHeader.Input.Builder labelIdBuilder = InferRequestHeader.Input.newBuilder();
        labelIdBuilder.setName("label_ids");
        InferRequestHeader.Input.Builder inputIdsBuilder = InferRequestHeader.Input.newBuilder();
        inputIdsBuilder.setName("input_ids");
        InferRequestHeader.Input.Builder inputMaskBuilder = InferRequestHeader.Input.newBuilder();
        inputMaskBuilder.setName("input_mask");
        InferRequestHeader.Input.Builder segmentIdsBuilder = InferRequestHeader.Input.newBuilder();
        segmentIdsBuilder.setName("segment_ids");

        InferRequestHeader.Output.Builder probabilitiesBuilder = InferRequestHeader.Output.newBuilder();
        probabilitiesBuilder.setName("probabilities");

        rhBuilder.addInput(labelIdBuilder);
        inferRequest.addRawInput(ByteString.copyFrom(intArrayToByteArray(labelId)));

        rhBuilder.addInput(inputIdsBuilder.build());
        inferRequest.addRawInput(ByteString.copyFrom(intArrayToByteArray(inputIds)));

        rhBuilder.addInput(inputMaskBuilder);
        inferRequest.addRawInput(ByteString.copyFrom(intArrayToByteArray(inputMask)));

        rhBuilder.addInput(segmentIdsBuilder);
        inferRequest.addRawInput(ByteString.copyFrom(intArrayToByteArray(segmentIds)));

        rhBuilder.addOutput(probabilitiesBuilder);
        rhBuilder.setBatchSize(batchSize);
        inferRequest.setMetaData(rhBuilder);

        InferRequest request = inferRequest.build();

        final ManagedChannel channel = ManagedChannelBuilder.forTarget("localhost:8001").usePlaintext().build();

        GRPCServiceGrpc.GRPCServiceStub stub = GRPCServiceGrpc.newStub(channel);
        stub.infer(request, new StreamObserver<GrpcServiceProto.InferResponse>() {
            public void onNext(GrpcServiceProto.InferResponse inferResponse) {
                byteArrayToFloatArray(inferResponse.getRawOutput(0).toByteArray());
            }

            public void onError(Throwable throwable) {

            }

            public void onCompleted() {
                // Typically you'll shutdown the channel somewhere else.
                // But for the purpose of the lab, we are only making a single
                // request. We'll shutdown as soon as this request is done.
                channel.shutdownNow();
                System.exit(0);
            }
        });

//        GRPCServiceGrpc.GRPCServiceBlockingStub blockingStub = GRPCServiceGrpc.newBlockingStub(channel);
//        GrpcServiceProto.InferResponse inferResponse = blockingStub.infer(request);
//        System.out.println(inferResponse.getMetaData());
//        System.out.println(inferResponse.getRequestStatus());
//
//        byteArrayToFloatArray(inferResponse.getRawOutput(0).toByteArray());
//        channel.shutdownNow();
    }

    public static void main(String[] args) throws InterruptedException {
        run();
        Thread.sleep(100000);
    }
}
