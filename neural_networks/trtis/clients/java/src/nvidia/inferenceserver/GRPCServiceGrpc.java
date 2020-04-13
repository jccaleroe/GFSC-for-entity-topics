package nvidia.inferenceserver;

import static io.grpc.MethodDescriptor.generateFullMethodName;
import static io.grpc.stub.ClientCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ClientCalls.asyncClientStreamingCall;
import static io.grpc.stub.ClientCalls.asyncServerStreamingCall;
import static io.grpc.stub.ClientCalls.asyncUnaryCall;
import static io.grpc.stub.ClientCalls.blockingServerStreamingCall;
import static io.grpc.stub.ClientCalls.blockingUnaryCall;
import static io.grpc.stub.ClientCalls.futureUnaryCall;
import static io.grpc.stub.ServerCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ServerCalls.asyncClientStreamingCall;
import static io.grpc.stub.ServerCalls.asyncServerStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnaryCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall;

/**
 * <pre>
 *&#64;&#64;
 *&#64;&#64;.. cpp:var:: service GRPCService
 *&#64;&#64;
 *&#64;&#64;   Inference Server GRPC endpoints.
 *&#64;&#64;
 * </pre>
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.23.0)",
    comments = "Source: grpc_service.proto")
public final class GRPCServiceGrpc {

  private GRPCServiceGrpc() {}

  public static final String SERVICE_NAME = "nvidia.inferenceserver.GRPCService";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.StatusRequest,
      nvidia.inferenceserver.GrpcServiceProto.StatusResponse> getStatusMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "Status",
      requestType = nvidia.inferenceserver.GrpcServiceProto.StatusRequest.class,
      responseType = nvidia.inferenceserver.GrpcServiceProto.StatusResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.StatusRequest,
      nvidia.inferenceserver.GrpcServiceProto.StatusResponse> getStatusMethod() {
    io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.StatusRequest, nvidia.inferenceserver.GrpcServiceProto.StatusResponse> getStatusMethod;
    if ((getStatusMethod = GRPCServiceGrpc.getStatusMethod) == null) {
      synchronized (GRPCServiceGrpc.class) {
        if ((getStatusMethod = GRPCServiceGrpc.getStatusMethod) == null) {
          GRPCServiceGrpc.getStatusMethod = getStatusMethod =
              io.grpc.MethodDescriptor.<nvidia.inferenceserver.GrpcServiceProto.StatusRequest, nvidia.inferenceserver.GrpcServiceProto.StatusResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "Status"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.StatusRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.StatusResponse.getDefaultInstance()))
              .setSchemaDescriptor(new GRPCServiceMethodDescriptorSupplier("Status"))
              .build();
        }
      }
    }
    return getStatusMethod;
  }

  private static volatile io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.ProfileRequest,
      nvidia.inferenceserver.GrpcServiceProto.ProfileResponse> getProfileMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "Profile",
      requestType = nvidia.inferenceserver.GrpcServiceProto.ProfileRequest.class,
      responseType = nvidia.inferenceserver.GrpcServiceProto.ProfileResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.ProfileRequest,
      nvidia.inferenceserver.GrpcServiceProto.ProfileResponse> getProfileMethod() {
    io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.ProfileRequest, nvidia.inferenceserver.GrpcServiceProto.ProfileResponse> getProfileMethod;
    if ((getProfileMethod = GRPCServiceGrpc.getProfileMethod) == null) {
      synchronized (GRPCServiceGrpc.class) {
        if ((getProfileMethod = GRPCServiceGrpc.getProfileMethod) == null) {
          GRPCServiceGrpc.getProfileMethod = getProfileMethod =
              io.grpc.MethodDescriptor.<nvidia.inferenceserver.GrpcServiceProto.ProfileRequest, nvidia.inferenceserver.GrpcServiceProto.ProfileResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "Profile"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.ProfileRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.ProfileResponse.getDefaultInstance()))
              .setSchemaDescriptor(new GRPCServiceMethodDescriptorSupplier("Profile"))
              .build();
        }
      }
    }
    return getProfileMethod;
  }

  private static volatile io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.HealthRequest,
      nvidia.inferenceserver.GrpcServiceProto.HealthResponse> getHealthMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "Health",
      requestType = nvidia.inferenceserver.GrpcServiceProto.HealthRequest.class,
      responseType = nvidia.inferenceserver.GrpcServiceProto.HealthResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.HealthRequest,
      nvidia.inferenceserver.GrpcServiceProto.HealthResponse> getHealthMethod() {
    io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.HealthRequest, nvidia.inferenceserver.GrpcServiceProto.HealthResponse> getHealthMethod;
    if ((getHealthMethod = GRPCServiceGrpc.getHealthMethod) == null) {
      synchronized (GRPCServiceGrpc.class) {
        if ((getHealthMethod = GRPCServiceGrpc.getHealthMethod) == null) {
          GRPCServiceGrpc.getHealthMethod = getHealthMethod =
              io.grpc.MethodDescriptor.<nvidia.inferenceserver.GrpcServiceProto.HealthRequest, nvidia.inferenceserver.GrpcServiceProto.HealthResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "Health"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.HealthRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.HealthResponse.getDefaultInstance()))
              .setSchemaDescriptor(new GRPCServiceMethodDescriptorSupplier("Health"))
              .build();
        }
      }
    }
    return getHealthMethod;
  }

  private static volatile io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.ModelControlRequest,
      nvidia.inferenceserver.GrpcServiceProto.ModelControlResponse> getModelControlMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "ModelControl",
      requestType = nvidia.inferenceserver.GrpcServiceProto.ModelControlRequest.class,
      responseType = nvidia.inferenceserver.GrpcServiceProto.ModelControlResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.ModelControlRequest,
      nvidia.inferenceserver.GrpcServiceProto.ModelControlResponse> getModelControlMethod() {
    io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.ModelControlRequest, nvidia.inferenceserver.GrpcServiceProto.ModelControlResponse> getModelControlMethod;
    if ((getModelControlMethod = GRPCServiceGrpc.getModelControlMethod) == null) {
      synchronized (GRPCServiceGrpc.class) {
        if ((getModelControlMethod = GRPCServiceGrpc.getModelControlMethod) == null) {
          GRPCServiceGrpc.getModelControlMethod = getModelControlMethod =
              io.grpc.MethodDescriptor.<nvidia.inferenceserver.GrpcServiceProto.ModelControlRequest, nvidia.inferenceserver.GrpcServiceProto.ModelControlResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "ModelControl"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.ModelControlRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.ModelControlResponse.getDefaultInstance()))
              .setSchemaDescriptor(new GRPCServiceMethodDescriptorSupplier("ModelControl"))
              .build();
        }
      }
    }
    return getModelControlMethod;
  }

  private static volatile io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlRequest,
      nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlResponse> getSharedMemoryControlMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "SharedMemoryControl",
      requestType = nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlRequest.class,
      responseType = nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlRequest,
      nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlResponse> getSharedMemoryControlMethod() {
    io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlRequest, nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlResponse> getSharedMemoryControlMethod;
    if ((getSharedMemoryControlMethod = GRPCServiceGrpc.getSharedMemoryControlMethod) == null) {
      synchronized (GRPCServiceGrpc.class) {
        if ((getSharedMemoryControlMethod = GRPCServiceGrpc.getSharedMemoryControlMethod) == null) {
          GRPCServiceGrpc.getSharedMemoryControlMethod = getSharedMemoryControlMethod =
              io.grpc.MethodDescriptor.<nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlRequest, nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "SharedMemoryControl"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlResponse.getDefaultInstance()))
              .setSchemaDescriptor(new GRPCServiceMethodDescriptorSupplier("SharedMemoryControl"))
              .build();
        }
      }
    }
    return getSharedMemoryControlMethod;
  }

  private static volatile io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.InferRequest,
      nvidia.inferenceserver.GrpcServiceProto.InferResponse> getInferMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "Infer",
      requestType = nvidia.inferenceserver.GrpcServiceProto.InferRequest.class,
      responseType = nvidia.inferenceserver.GrpcServiceProto.InferResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.InferRequest,
      nvidia.inferenceserver.GrpcServiceProto.InferResponse> getInferMethod() {
    io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.InferRequest, nvidia.inferenceserver.GrpcServiceProto.InferResponse> getInferMethod;
    if ((getInferMethod = GRPCServiceGrpc.getInferMethod) == null) {
      synchronized (GRPCServiceGrpc.class) {
        if ((getInferMethod = GRPCServiceGrpc.getInferMethod) == null) {
          GRPCServiceGrpc.getInferMethod = getInferMethod =
              io.grpc.MethodDescriptor.<nvidia.inferenceserver.GrpcServiceProto.InferRequest, nvidia.inferenceserver.GrpcServiceProto.InferResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "Infer"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.InferRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.InferResponse.getDefaultInstance()))
              .setSchemaDescriptor(new GRPCServiceMethodDescriptorSupplier("Infer"))
              .build();
        }
      }
    }
    return getInferMethod;
  }

  private static volatile io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.InferRequest,
      nvidia.inferenceserver.GrpcServiceProto.InferResponse> getStreamInferMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "StreamInfer",
      requestType = nvidia.inferenceserver.GrpcServiceProto.InferRequest.class,
      responseType = nvidia.inferenceserver.GrpcServiceProto.InferResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.BIDI_STREAMING)
  public static io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.InferRequest,
      nvidia.inferenceserver.GrpcServiceProto.InferResponse> getStreamInferMethod() {
    io.grpc.MethodDescriptor<nvidia.inferenceserver.GrpcServiceProto.InferRequest, nvidia.inferenceserver.GrpcServiceProto.InferResponse> getStreamInferMethod;
    if ((getStreamInferMethod = GRPCServiceGrpc.getStreamInferMethod) == null) {
      synchronized (GRPCServiceGrpc.class) {
        if ((getStreamInferMethod = GRPCServiceGrpc.getStreamInferMethod) == null) {
          GRPCServiceGrpc.getStreamInferMethod = getStreamInferMethod =
              io.grpc.MethodDescriptor.<nvidia.inferenceserver.GrpcServiceProto.InferRequest, nvidia.inferenceserver.GrpcServiceProto.InferResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.BIDI_STREAMING)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "StreamInfer"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.InferRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  nvidia.inferenceserver.GrpcServiceProto.InferResponse.getDefaultInstance()))
              .setSchemaDescriptor(new GRPCServiceMethodDescriptorSupplier("StreamInfer"))
              .build();
        }
      }
    }
    return getStreamInferMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static GRPCServiceStub newStub(io.grpc.Channel channel) {
    return new GRPCServiceStub(channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static GRPCServiceBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    return new GRPCServiceBlockingStub(channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static GRPCServiceFutureStub newFutureStub(
      io.grpc.Channel channel) {
    return new GRPCServiceFutureStub(channel);
  }

  /**
   * <pre>
   *&#64;&#64;
   *&#64;&#64;.. cpp:var:: service GRPCService
   *&#64;&#64;
   *&#64;&#64;   Inference Server GRPC endpoints.
   *&#64;&#64;
   * </pre>
   */
  public static abstract class GRPCServiceImplBase implements io.grpc.BindableService {

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Status(StatusRequest) returns (StatusResponse)
     *&#64;&#64;
     *&#64;&#64;     Get status for entire inference server or for a specified model.
     *&#64;&#64;
     * </pre>
     */
    public void status(nvidia.inferenceserver.GrpcServiceProto.StatusRequest request,
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.StatusResponse> responseObserver) {
      asyncUnimplementedUnaryCall(getStatusMethod(), responseObserver);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Profile(ProfileRequest) returns (ProfileResponse)
     *&#64;&#64;
     *&#64;&#64;     Enable and disable low-level GPU profiling.
     *&#64;&#64;
     * </pre>
     */
    public void profile(nvidia.inferenceserver.GrpcServiceProto.ProfileRequest request,
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.ProfileResponse> responseObserver) {
      asyncUnimplementedUnaryCall(getProfileMethod(), responseObserver);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Health(HealthRequest) returns (HealthResponse)
     *&#64;&#64;
     *&#64;&#64;     Check liveness and readiness of the inference server.
     *&#64;&#64;
     * </pre>
     */
    public void health(nvidia.inferenceserver.GrpcServiceProto.HealthRequest request,
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.HealthResponse> responseObserver) {
      asyncUnimplementedUnaryCall(getHealthMethod(), responseObserver);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc ModelControl(ModelControlRequest) returns
     *&#64;&#64;     (ModelControlResponse)
     *&#64;&#64;
     *&#64;&#64;     Request to load / unload a specified model.
     *&#64;&#64;
     * </pre>
     */
    public void modelControl(nvidia.inferenceserver.GrpcServiceProto.ModelControlRequest request,
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.ModelControlResponse> responseObserver) {
      asyncUnimplementedUnaryCall(getModelControlMethod(), responseObserver);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc SharedMemoryControl(SharedMemoryControlRequest) returns
     *&#64;&#64;     (SharedMemoryControlResponse)
     *&#64;&#64;
     *&#64;&#64;     Request to register / unregister a specified shared memory region.
     *&#64;&#64;
     * </pre>
     */
    public void sharedMemoryControl(nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlRequest request,
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlResponse> responseObserver) {
      asyncUnimplementedUnaryCall(getSharedMemoryControlMethod(), responseObserver);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Infer(InferRequest) returns (InferResponse)
     *&#64;&#64;
     *&#64;&#64;     Request inference using a specific model. [ To handle large input
     *&#64;&#64;     tensors likely need to set the maximum message size to that they
     *&#64;&#64;     can be transmitted in one pass.
     *&#64;&#64;
     * </pre>
     */
    public void infer(nvidia.inferenceserver.GrpcServiceProto.InferRequest request,
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.InferResponse> responseObserver) {
      asyncUnimplementedUnaryCall(getInferMethod(), responseObserver);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc StreamInfer(stream InferRequest) returns (stream
     *&#64;&#64;     InferResponse)
     *&#64;&#64;
     *&#64;&#64;     Request inferences using a specific model in a streaming manner.
     *&#64;&#64;     Individual inference requests sent through the same stream will be
     *&#64;&#64;     processed in order and be returned on completion
     *&#64;&#64;
     * </pre>
     */
    public io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.InferRequest> streamInfer(
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.InferResponse> responseObserver) {
      return asyncUnimplementedStreamingCall(getStreamInferMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getStatusMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                nvidia.inferenceserver.GrpcServiceProto.StatusRequest,
                nvidia.inferenceserver.GrpcServiceProto.StatusResponse>(
                  this, METHODID_STATUS)))
          .addMethod(
            getProfileMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                nvidia.inferenceserver.GrpcServiceProto.ProfileRequest,
                nvidia.inferenceserver.GrpcServiceProto.ProfileResponse>(
                  this, METHODID_PROFILE)))
          .addMethod(
            getHealthMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                nvidia.inferenceserver.GrpcServiceProto.HealthRequest,
                nvidia.inferenceserver.GrpcServiceProto.HealthResponse>(
                  this, METHODID_HEALTH)))
          .addMethod(
            getModelControlMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                nvidia.inferenceserver.GrpcServiceProto.ModelControlRequest,
                nvidia.inferenceserver.GrpcServiceProto.ModelControlResponse>(
                  this, METHODID_MODEL_CONTROL)))
          .addMethod(
            getSharedMemoryControlMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlRequest,
                nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlResponse>(
                  this, METHODID_SHARED_MEMORY_CONTROL)))
          .addMethod(
            getInferMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                nvidia.inferenceserver.GrpcServiceProto.InferRequest,
                nvidia.inferenceserver.GrpcServiceProto.InferResponse>(
                  this, METHODID_INFER)))
          .addMethod(
            getStreamInferMethod(),
            asyncBidiStreamingCall(
              new MethodHandlers<
                nvidia.inferenceserver.GrpcServiceProto.InferRequest,
                nvidia.inferenceserver.GrpcServiceProto.InferResponse>(
                  this, METHODID_STREAM_INFER)))
          .build();
    }
  }

  /**
   * <pre>
   *&#64;&#64;
   *&#64;&#64;.. cpp:var:: service GRPCService
   *&#64;&#64;
   *&#64;&#64;   Inference Server GRPC endpoints.
   *&#64;&#64;
   * </pre>
   */
  public static final class GRPCServiceStub extends io.grpc.stub.AbstractStub<GRPCServiceStub> {
    private GRPCServiceStub(io.grpc.Channel channel) {
      super(channel);
    }

    private GRPCServiceStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GRPCServiceStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new GRPCServiceStub(channel, callOptions);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Status(StatusRequest) returns (StatusResponse)
     *&#64;&#64;
     *&#64;&#64;     Get status for entire inference server or for a specified model.
     *&#64;&#64;
     * </pre>
     */
    public void status(nvidia.inferenceserver.GrpcServiceProto.StatusRequest request,
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.StatusResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getStatusMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Profile(ProfileRequest) returns (ProfileResponse)
     *&#64;&#64;
     *&#64;&#64;     Enable and disable low-level GPU profiling.
     *&#64;&#64;
     * </pre>
     */
    public void profile(nvidia.inferenceserver.GrpcServiceProto.ProfileRequest request,
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.ProfileResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getProfileMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Health(HealthRequest) returns (HealthResponse)
     *&#64;&#64;
     *&#64;&#64;     Check liveness and readiness of the inference server.
     *&#64;&#64;
     * </pre>
     */
    public void health(nvidia.inferenceserver.GrpcServiceProto.HealthRequest request,
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.HealthResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getHealthMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc ModelControl(ModelControlRequest) returns
     *&#64;&#64;     (ModelControlResponse)
     *&#64;&#64;
     *&#64;&#64;     Request to load / unload a specified model.
     *&#64;&#64;
     * </pre>
     */
    public void modelControl(nvidia.inferenceserver.GrpcServiceProto.ModelControlRequest request,
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.ModelControlResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getModelControlMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc SharedMemoryControl(SharedMemoryControlRequest) returns
     *&#64;&#64;     (SharedMemoryControlResponse)
     *&#64;&#64;
     *&#64;&#64;     Request to register / unregister a specified shared memory region.
     *&#64;&#64;
     * </pre>
     */
    public void sharedMemoryControl(nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlRequest request,
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getSharedMemoryControlMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Infer(InferRequest) returns (InferResponse)
     *&#64;&#64;
     *&#64;&#64;     Request inference using a specific model. [ To handle large input
     *&#64;&#64;     tensors likely need to set the maximum message size to that they
     *&#64;&#64;     can be transmitted in one pass.
     *&#64;&#64;
     * </pre>
     */
    public void infer(nvidia.inferenceserver.GrpcServiceProto.InferRequest request,
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.InferResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getInferMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc StreamInfer(stream InferRequest) returns (stream
     *&#64;&#64;     InferResponse)
     *&#64;&#64;
     *&#64;&#64;     Request inferences using a specific model in a streaming manner.
     *&#64;&#64;     Individual inference requests sent through the same stream will be
     *&#64;&#64;     processed in order and be returned on completion
     *&#64;&#64;
     * </pre>
     */
    public io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.InferRequest> streamInfer(
        io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.InferResponse> responseObserver) {
      return asyncBidiStreamingCall(
          getChannel().newCall(getStreamInferMethod(), getCallOptions()), responseObserver);
    }
  }

  /**
   * <pre>
   *&#64;&#64;
   *&#64;&#64;.. cpp:var:: service GRPCService
   *&#64;&#64;
   *&#64;&#64;   Inference Server GRPC endpoints.
   *&#64;&#64;
   * </pre>
   */
  public static final class GRPCServiceBlockingStub extends io.grpc.stub.AbstractStub<GRPCServiceBlockingStub> {
    private GRPCServiceBlockingStub(io.grpc.Channel channel) {
      super(channel);
    }

    private GRPCServiceBlockingStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GRPCServiceBlockingStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new GRPCServiceBlockingStub(channel, callOptions);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Status(StatusRequest) returns (StatusResponse)
     *&#64;&#64;
     *&#64;&#64;     Get status for entire inference server or for a specified model.
     *&#64;&#64;
     * </pre>
     */
    public nvidia.inferenceserver.GrpcServiceProto.StatusResponse status(nvidia.inferenceserver.GrpcServiceProto.StatusRequest request) {
      return blockingUnaryCall(
          getChannel(), getStatusMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Profile(ProfileRequest) returns (ProfileResponse)
     *&#64;&#64;
     *&#64;&#64;     Enable and disable low-level GPU profiling.
     *&#64;&#64;
     * </pre>
     */
    public nvidia.inferenceserver.GrpcServiceProto.ProfileResponse profile(nvidia.inferenceserver.GrpcServiceProto.ProfileRequest request) {
      return blockingUnaryCall(
          getChannel(), getProfileMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Health(HealthRequest) returns (HealthResponse)
     *&#64;&#64;
     *&#64;&#64;     Check liveness and readiness of the inference server.
     *&#64;&#64;
     * </pre>
     */
    public nvidia.inferenceserver.GrpcServiceProto.HealthResponse health(nvidia.inferenceserver.GrpcServiceProto.HealthRequest request) {
      return blockingUnaryCall(
          getChannel(), getHealthMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc ModelControl(ModelControlRequest) returns
     *&#64;&#64;     (ModelControlResponse)
     *&#64;&#64;
     *&#64;&#64;     Request to load / unload a specified model.
     *&#64;&#64;
     * </pre>
     */
    public nvidia.inferenceserver.GrpcServiceProto.ModelControlResponse modelControl(nvidia.inferenceserver.GrpcServiceProto.ModelControlRequest request) {
      return blockingUnaryCall(
          getChannel(), getModelControlMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc SharedMemoryControl(SharedMemoryControlRequest) returns
     *&#64;&#64;     (SharedMemoryControlResponse)
     *&#64;&#64;
     *&#64;&#64;     Request to register / unregister a specified shared memory region.
     *&#64;&#64;
     * </pre>
     */
    public nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlResponse sharedMemoryControl(nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlRequest request) {
      return blockingUnaryCall(
          getChannel(), getSharedMemoryControlMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Infer(InferRequest) returns (InferResponse)
     *&#64;&#64;
     *&#64;&#64;     Request inference using a specific model. [ To handle large input
     *&#64;&#64;     tensors likely need to set the maximum message size to that they
     *&#64;&#64;     can be transmitted in one pass.
     *&#64;&#64;
     * </pre>
     */
    public nvidia.inferenceserver.GrpcServiceProto.InferResponse infer(nvidia.inferenceserver.GrpcServiceProto.InferRequest request) {
      return blockingUnaryCall(
          getChannel(), getInferMethod(), getCallOptions(), request);
    }
  }

  /**
   * <pre>
   *&#64;&#64;
   *&#64;&#64;.. cpp:var:: service GRPCService
   *&#64;&#64;
   *&#64;&#64;   Inference Server GRPC endpoints.
   *&#64;&#64;
   * </pre>
   */
  public static final class GRPCServiceFutureStub extends io.grpc.stub.AbstractStub<GRPCServiceFutureStub> {
    private GRPCServiceFutureStub(io.grpc.Channel channel) {
      super(channel);
    }

    private GRPCServiceFutureStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GRPCServiceFutureStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new GRPCServiceFutureStub(channel, callOptions);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Status(StatusRequest) returns (StatusResponse)
     *&#64;&#64;
     *&#64;&#64;     Get status for entire inference server or for a specified model.
     *&#64;&#64;
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<nvidia.inferenceserver.GrpcServiceProto.StatusResponse> status(
        nvidia.inferenceserver.GrpcServiceProto.StatusRequest request) {
      return futureUnaryCall(
          getChannel().newCall(getStatusMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Profile(ProfileRequest) returns (ProfileResponse)
     *&#64;&#64;
     *&#64;&#64;     Enable and disable low-level GPU profiling.
     *&#64;&#64;
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<nvidia.inferenceserver.GrpcServiceProto.ProfileResponse> profile(
        nvidia.inferenceserver.GrpcServiceProto.ProfileRequest request) {
      return futureUnaryCall(
          getChannel().newCall(getProfileMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Health(HealthRequest) returns (HealthResponse)
     *&#64;&#64;
     *&#64;&#64;     Check liveness and readiness of the inference server.
     *&#64;&#64;
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<nvidia.inferenceserver.GrpcServiceProto.HealthResponse> health(
        nvidia.inferenceserver.GrpcServiceProto.HealthRequest request) {
      return futureUnaryCall(
          getChannel().newCall(getHealthMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc ModelControl(ModelControlRequest) returns
     *&#64;&#64;     (ModelControlResponse)
     *&#64;&#64;
     *&#64;&#64;     Request to load / unload a specified model.
     *&#64;&#64;
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<nvidia.inferenceserver.GrpcServiceProto.ModelControlResponse> modelControl(
        nvidia.inferenceserver.GrpcServiceProto.ModelControlRequest request) {
      return futureUnaryCall(
          getChannel().newCall(getModelControlMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc SharedMemoryControl(SharedMemoryControlRequest) returns
     *&#64;&#64;     (SharedMemoryControlResponse)
     *&#64;&#64;
     *&#64;&#64;     Request to register / unregister a specified shared memory region.
     *&#64;&#64;
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlResponse> sharedMemoryControl(
        nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlRequest request) {
      return futureUnaryCall(
          getChannel().newCall(getSharedMemoryControlMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     *&#64;&#64;  .. cpp:var:: rpc Infer(InferRequest) returns (InferResponse)
     *&#64;&#64;
     *&#64;&#64;     Request inference using a specific model. [ To handle large input
     *&#64;&#64;     tensors likely need to set the maximum message size to that they
     *&#64;&#64;     can be transmitted in one pass.
     *&#64;&#64;
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<nvidia.inferenceserver.GrpcServiceProto.InferResponse> infer(
        nvidia.inferenceserver.GrpcServiceProto.InferRequest request) {
      return futureUnaryCall(
          getChannel().newCall(getInferMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_STATUS = 0;
  private static final int METHODID_PROFILE = 1;
  private static final int METHODID_HEALTH = 2;
  private static final int METHODID_MODEL_CONTROL = 3;
  private static final int METHODID_SHARED_MEMORY_CONTROL = 4;
  private static final int METHODID_INFER = 5;
  private static final int METHODID_STREAM_INFER = 6;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final GRPCServiceImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(GRPCServiceImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_STATUS:
          serviceImpl.status((nvidia.inferenceserver.GrpcServiceProto.StatusRequest) request,
              (io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.StatusResponse>) responseObserver);
          break;
        case METHODID_PROFILE:
          serviceImpl.profile((nvidia.inferenceserver.GrpcServiceProto.ProfileRequest) request,
              (io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.ProfileResponse>) responseObserver);
          break;
        case METHODID_HEALTH:
          serviceImpl.health((nvidia.inferenceserver.GrpcServiceProto.HealthRequest) request,
              (io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.HealthResponse>) responseObserver);
          break;
        case METHODID_MODEL_CONTROL:
          serviceImpl.modelControl((nvidia.inferenceserver.GrpcServiceProto.ModelControlRequest) request,
              (io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.ModelControlResponse>) responseObserver);
          break;
        case METHODID_SHARED_MEMORY_CONTROL:
          serviceImpl.sharedMemoryControl((nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlRequest) request,
              (io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.SharedMemoryControlResponse>) responseObserver);
          break;
        case METHODID_INFER:
          serviceImpl.infer((nvidia.inferenceserver.GrpcServiceProto.InferRequest) request,
              (io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.InferResponse>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_STREAM_INFER:
          return (io.grpc.stub.StreamObserver<Req>) serviceImpl.streamInfer(
              (io.grpc.stub.StreamObserver<nvidia.inferenceserver.GrpcServiceProto.InferResponse>) responseObserver);
        default:
          throw new AssertionError();
      }
    }
  }

  private static abstract class GRPCServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    GRPCServiceBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return nvidia.inferenceserver.GrpcServiceProto.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("GRPCService");
    }
  }

  private static final class GRPCServiceFileDescriptorSupplier
      extends GRPCServiceBaseDescriptorSupplier {
    GRPCServiceFileDescriptorSupplier() {}
  }

  private static final class GRPCServiceMethodDescriptorSupplier
      extends GRPCServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    GRPCServiceMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (GRPCServiceGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new GRPCServiceFileDescriptorSupplier())
              .addMethod(getStatusMethod())
              .addMethod(getProfileMethod())
              .addMethod(getHealthMethod())
              .addMethod(getModelControlMethod())
              .addMethod(getSharedMemoryControlMethod())
              .addMethod(getInferMethod())
              .addMethod(getStreamInferMethod())
              .build();
        }
      }
    }
    return result;
  }
}
