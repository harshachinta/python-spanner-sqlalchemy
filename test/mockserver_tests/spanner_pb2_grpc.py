# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!

# Generated with the following commands:
#
# pip install grpcio-tools
# git clone git@github.com:googleapis/googleapis.git
# cd googleapis
# python -m grpc_tools.protoc \
#     -I . \
#     --python_out=. --pyi_out=. --grpc_python_out=. \
#     ./google/spanner/v1/*.proto

# flake8: noqa

"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.cloud.spanner_v1.types import (
    commit_response as google_dot_spanner_dot_v1_dot_commit__response__pb2,
)
from google.cloud.spanner_v1.types import (
    result_set as google_dot_spanner_dot_v1_dot_result__set__pb2,
)
from google.cloud.spanner_v1.types import (
    spanner as google_dot_spanner_dot_v1_dot_spanner__pb2,
)
from google.cloud.spanner_v1.types import (
    transaction as google_dot_spanner_dot_v1_dot_transaction__pb2,
)

GRPC_GENERATED_VERSION = "1.67.0"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in google/spanner/v1/spanner_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class SpannerServicer(object):
    """Cloud Spanner API

    The Cloud Spanner API can be used to manage sessions and execute
    transactions on data stored in Cloud Spanner databases.
    """

    def CreateSession(self, request, context):
        """Creates a new session. A session can be used to perform
        transactions that read and/or modify data in a Cloud Spanner database.
        Sessions are meant to be reused for many consecutive
        transactions.

        Sessions can only execute one transaction at a time. To execute
        multiple concurrent read-write/write-only transactions, create
        multiple sessions. Note that standalone reads and queries use a
        transaction internally, and count toward the one transaction
        limit.

        Active sessions use additional server resources, so it is a good idea to
        delete idle and unneeded sessions.
        Aside from explicit deletes, Cloud Spanner may delete sessions for which no
        operations are sent for more than an hour. If a session is deleted,
        requests to it return `NOT_FOUND`.

        Idle sessions can be kept alive by sending a trivial SQL query
        periodically, e.g., `"SELECT 1"`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BatchCreateSessions(self, request, context):
        """Creates multiple new sessions.

        This API can be used to initialize a session cache on the clients.
        See https://goo.gl/TgSFN2 for best practices on session cache management.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetSession(self, request, context):
        """Gets a session. Returns `NOT_FOUND` if the session does not exist.
        This is mainly useful for determining whether a session is still
        alive.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListSessions(self, request, context):
        """Lists all sessions in a given database."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteSession(self, request, context):
        """Ends a session, releasing server resources associated with it. This will
        asynchronously trigger cancellation of any operations that are running with
        this session.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExecuteSql(self, request, context):
        """Executes an SQL statement, returning all results in a single reply. This
        method cannot be used to return a result set larger than 10 MiB;
        if the query yields more data than that, the query fails with
        a `FAILED_PRECONDITION` error.

        Operations inside read-write transactions might return `ABORTED`. If
        this occurs, the application should restart the transaction from
        the beginning. See [Transaction][google.spanner.v1.Transaction] for more
        details.

        Larger result sets can be fetched in streaming fashion by calling
        [ExecuteStreamingSql][google.spanner.v1.Spanner.ExecuteStreamingSql]
        instead.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExecuteStreamingSql(self, request, context):
        """Like [ExecuteSql][google.spanner.v1.Spanner.ExecuteSql], except returns the
        result set as a stream. Unlike
        [ExecuteSql][google.spanner.v1.Spanner.ExecuteSql], there is no limit on
        the size of the returned result set. However, no individual row in the
        result set can exceed 100 MiB, and no column value can exceed 10 MiB.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExecuteBatchDml(self, request, context):
        """Executes a batch of SQL DML statements. This method allows many statements
        to be run with lower latency than submitting them sequentially with
        [ExecuteSql][google.spanner.v1.Spanner.ExecuteSql].

        Statements are executed in sequential order. A request can succeed even if
        a statement fails. The
        [ExecuteBatchDmlResponse.status][google.spanner.v1.ExecuteBatchDmlResponse.status]
        field in the response provides information about the statement that failed.
        Clients must inspect this field to determine whether an error occurred.

        Execution stops after the first failed statement; the remaining statements
        are not executed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Read(self, request, context):
        """Reads rows from the database using key lookups and scans, as a
        simple key/value style alternative to
        [ExecuteSql][google.spanner.v1.Spanner.ExecuteSql].  This method cannot be
        used to return a result set larger than 10 MiB; if the read matches more
        data than that, the read fails with a `FAILED_PRECONDITION`
        error.

        Reads inside read-write transactions might return `ABORTED`. If
        this occurs, the application should restart the transaction from
        the beginning. See [Transaction][google.spanner.v1.Transaction] for more
        details.

        Larger result sets can be yielded in streaming fashion by calling
        [StreamingRead][google.spanner.v1.Spanner.StreamingRead] instead.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StreamingRead(self, request, context):
        """Like [Read][google.spanner.v1.Spanner.Read], except returns the result set
        as a stream. Unlike [Read][google.spanner.v1.Spanner.Read], there is no
        limit on the size of the returned result set. However, no individual row in
        the result set can exceed 100 MiB, and no column value can exceed
        10 MiB.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BeginTransaction(self, request, context):
        """Begins a new transaction. This step can often be skipped:
        [Read][google.spanner.v1.Spanner.Read],
        [ExecuteSql][google.spanner.v1.Spanner.ExecuteSql] and
        [Commit][google.spanner.v1.Spanner.Commit] can begin a new transaction as a
        side-effect.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Commit(self, request, context):
        """Commits a transaction. The request includes the mutations to be
        applied to rows in the database.

        `Commit` might return an `ABORTED` error. This can occur at any time;
        commonly, the cause is conflicts with concurrent
        transactions. However, it can also happen for a variety of other
        reasons. If `Commit` returns `ABORTED`, the caller should re-attempt
        the transaction from the beginning, re-using the same session.

        On very rare occasions, `Commit` might return `UNKNOWN`. This can happen,
        for example, if the client job experiences a 1+ hour networking failure.
        At that point, Cloud Spanner has lost track of the transaction outcome and
        we recommend that you perform another read from the database to see the
        state of things as they are now.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Rollback(self, request, context):
        """Rolls back a transaction, releasing any locks it holds. It is a good
        idea to call this for any transaction that includes one or more
        [Read][google.spanner.v1.Spanner.Read] or
        [ExecuteSql][google.spanner.v1.Spanner.ExecuteSql] requests and ultimately
        decides not to commit.

        `Rollback` returns `OK` if it successfully aborts the transaction, the
        transaction was already aborted, or the transaction is not
        found. `Rollback` never returns `ABORTED`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PartitionQuery(self, request, context):
        """Creates a set of partition tokens that can be used to execute a query
        operation in parallel.  Each of the returned partition tokens can be used
        by [ExecuteStreamingSql][google.spanner.v1.Spanner.ExecuteStreamingSql] to
        specify a subset of the query result to read.  The same session and
        read-only transaction must be used by the PartitionQueryRequest used to
        create the partition tokens and the ExecuteSqlRequests that use the
        partition tokens.

        Partition tokens become invalid when the session used to create them
        is deleted, is idle for too long, begins a new transaction, or becomes too
        old.  When any of these happen, it is not possible to resume the query, and
        the whole operation must be restarted from the beginning.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PartitionRead(self, request, context):
        """Creates a set of partition tokens that can be used to execute a read
        operation in parallel.  Each of the returned partition tokens can be used
        by [StreamingRead][google.spanner.v1.Spanner.StreamingRead] to specify a
        subset of the read result to read.  The same session and read-only
        transaction must be used by the PartitionReadRequest used to create the
        partition tokens and the ReadRequests that use the partition tokens.  There
        are no ordering guarantees on rows returned among the returned partition
        tokens, or even within each individual StreamingRead call issued with a
        partition_token.

        Partition tokens become invalid when the session used to create them
        is deleted, is idle for too long, begins a new transaction, or becomes too
        old.  When any of these happen, it is not possible to resume the read, and
        the whole operation must be restarted from the beginning.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BatchWrite(self, request, context):
        """Batches the supplied mutation groups in a collection of efficient
        transactions. All mutations in a group are committed atomically. However,
        mutations across groups can be committed non-atomically in an unspecified
        order and thus, they must be independent of each other. Partial failure is
        possible, i.e., some groups may have been committed successfully, while
        some may have failed. The results of individual batches are streamed into
        the response as the batches are applied.

        BatchWrite requests are not replay protected, meaning that each mutation
        group may be applied more than once. Replays of non-idempotent mutations
        may have undesirable effects. For example, replays of an insert mutation
        may produce an already exists error or if you use generated or commit
        timestamp-based keys, it may result in additional rows being added to the
        mutation's table. We recommend structuring your mutation groups to be
        idempotent to avoid this issue.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SpannerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateSession": grpc.unary_unary_rpc_method_handler(
            servicer.CreateSession,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.CreateSessionRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_spanner__pb2.Session.serialize,
        ),
        "BatchCreateSessions": grpc.unary_unary_rpc_method_handler(
            servicer.BatchCreateSessions,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.BatchCreateSessionsRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_spanner__pb2.BatchCreateSessionsResponse.serialize,
        ),
        "GetSession": grpc.unary_unary_rpc_method_handler(
            servicer.GetSession,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.GetSessionRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_spanner__pb2.Session.serialize,
        ),
        "ListSessions": grpc.unary_unary_rpc_method_handler(
            servicer.ListSessions,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.ListSessionsRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_spanner__pb2.ListSessionsResponse.serialize,
        ),
        "DeleteSession": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteSession,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.DeleteSessionRequest.deserialize,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "ExecuteSql": grpc.unary_unary_rpc_method_handler(
            servicer.ExecuteSql,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.ExecuteSqlRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_result__set__pb2.ResultSet.serialize,
        ),
        "ExecuteStreamingSql": grpc.unary_stream_rpc_method_handler(
            servicer.ExecuteStreamingSql,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.ExecuteSqlRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_result__set__pb2.PartialResultSet.serialize,
        ),
        "ExecuteBatchDml": grpc.unary_unary_rpc_method_handler(
            servicer.ExecuteBatchDml,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.ExecuteBatchDmlRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_spanner__pb2.ExecuteBatchDmlResponse.serialize,
        ),
        "Read": grpc.unary_unary_rpc_method_handler(
            servicer.Read,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.ReadRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_result__set__pb2.ResultSet.serialize,
        ),
        "StreamingRead": grpc.unary_stream_rpc_method_handler(
            servicer.StreamingRead,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.ReadRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_result__set__pb2.PartialResultSet.serialize,
        ),
        "BeginTransaction": grpc.unary_unary_rpc_method_handler(
            servicer.BeginTransaction,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.BeginTransactionRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_transaction__pb2.Transaction.serialize,
        ),
        "Commit": grpc.unary_unary_rpc_method_handler(
            servicer.Commit,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.CommitRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_commit__response__pb2.CommitResponse.serialize,
        ),
        "Rollback": grpc.unary_unary_rpc_method_handler(
            servicer.Rollback,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.RollbackRequest.deserialize,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "PartitionQuery": grpc.unary_unary_rpc_method_handler(
            servicer.PartitionQuery,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.PartitionQueryRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_spanner__pb2.PartitionResponse.serialize,
        ),
        "PartitionRead": grpc.unary_unary_rpc_method_handler(
            servicer.PartitionRead,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.PartitionReadRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_spanner__pb2.PartitionResponse.serialize,
        ),
        "BatchWrite": grpc.unary_stream_rpc_method_handler(
            servicer.BatchWrite,
            request_deserializer=google_dot_spanner_dot_v1_dot_spanner__pb2.BatchWriteRequest.deserialize,
            response_serializer=google_dot_spanner_dot_v1_dot_spanner__pb2.BatchWriteResponse.serialize,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.spanner.v1.Spanner", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers(
        "google.spanner.v1.Spanner", rpc_method_handlers
    )


# This class is part of an EXPERIMENTAL API.
class Spanner(object):
    """Cloud Spanner API

    The Cloud Spanner API can be used to manage sessions and execute
    transactions on data stored in Cloud Spanner databases.
    """

    @staticmethod
    def CreateSession(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.spanner.v1.Spanner/CreateSession",
            google_dot_spanner_dot_v1_dot_spanner__pb2.CreateSessionRequest.to_json,
            google_dot_spanner_dot_v1_dot_spanner__pb2.Session.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def BatchCreateSessions(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.spanner.v1.Spanner/BatchCreateSessions",
            google_dot_spanner_dot_v1_dot_spanner__pb2.BatchCreateSessionsRequest.to_json,
            google_dot_spanner_dot_v1_dot_spanner__pb2.BatchCreateSessionsResponse.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def GetSession(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.spanner.v1.Spanner/GetSession",
            google_dot_spanner_dot_v1_dot_spanner__pb2.GetSessionRequest.to_json,
            google_dot_spanner_dot_v1_dot_spanner__pb2.Session.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def ListSessions(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.spanner.v1.Spanner/ListSessions",
            google_dot_spanner_dot_v1_dot_spanner__pb2.ListSessionsRequest.to_json,
            google_dot_spanner_dot_v1_dot_spanner__pb2.ListSessionsResponse.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def DeleteSession(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.spanner.v1.Spanner/DeleteSession",
            google_dot_spanner_dot_v1_dot_spanner__pb2.DeleteSessionRequest.to_json,
            google_dot_protobuf_dot_empty__pb2.Empty.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def ExecuteSql(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.spanner.v1.Spanner/ExecuteSql",
            google_dot_spanner_dot_v1_dot_spanner__pb2.ExecuteSqlRequest.to_json,
            google_dot_spanner_dot_v1_dot_result__set__pb2.ResultSet.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def ExecuteStreamingSql(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/google.spanner.v1.Spanner/ExecuteStreamingSql",
            google_dot_spanner_dot_v1_dot_spanner__pb2.ExecuteSqlRequest.to_json,
            google_dot_spanner_dot_v1_dot_result__set__pb2.PartialResultSet.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def ExecuteBatchDml(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.spanner.v1.Spanner/ExecuteBatchDml",
            google_dot_spanner_dot_v1_dot_spanner__pb2.ExecuteBatchDmlRequest.to_json,
            google_dot_spanner_dot_v1_dot_spanner__pb2.ExecuteBatchDmlResponse.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Read(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.spanner.v1.Spanner/Read",
            google_dot_spanner_dot_v1_dot_spanner__pb2.ReadRequest.to_json,
            google_dot_spanner_dot_v1_dot_result__set__pb2.ResultSet.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def StreamingRead(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/google.spanner.v1.Spanner/StreamingRead",
            google_dot_spanner_dot_v1_dot_spanner__pb2.ReadRequest.to_json,
            google_dot_spanner_dot_v1_dot_result__set__pb2.PartialResultSet.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def BeginTransaction(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.spanner.v1.Spanner/BeginTransaction",
            google_dot_spanner_dot_v1_dot_spanner__pb2.BeginTransactionRequest.to_json,
            google_dot_spanner_dot_v1_dot_transaction__pb2.Transaction.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Commit(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.spanner.v1.Spanner/Commit",
            google_dot_spanner_dot_v1_dot_spanner__pb2.CommitRequest.to_json,
            google_dot_spanner_dot_v1_dot_commit__response__pb2.CommitResponse.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Rollback(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.spanner.v1.Spanner/Rollback",
            google_dot_spanner_dot_v1_dot_spanner__pb2.RollbackRequest.to_json,
            google_dot_protobuf_dot_empty__pb2.Empty.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def PartitionQuery(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.spanner.v1.Spanner/PartitionQuery",
            google_dot_spanner_dot_v1_dot_spanner__pb2.PartitionQueryRequest.to_json,
            google_dot_spanner_dot_v1_dot_spanner__pb2.PartitionResponse.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def PartitionRead(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.spanner.v1.Spanner/PartitionRead",
            google_dot_spanner_dot_v1_dot_spanner__pb2.PartitionReadRequest.to_json,
            google_dot_spanner_dot_v1_dot_spanner__pb2.PartitionResponse.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def BatchWrite(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/google.spanner.v1.Spanner/BatchWrite",
            google_dot_spanner_dot_v1_dot_spanner__pb2.BatchWriteRequest.to_json,
            google_dot_spanner_dot_v1_dot_spanner__pb2.BatchWriteResponse.from_json,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
