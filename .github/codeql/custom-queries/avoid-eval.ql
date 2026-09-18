/**
 * Finds direct calls to Python's eval function.
 *
 * This is intentionally small so it can be used as a CodeQL learning example.
 */
import python

from Call call, Name functionName
where
  call.getFunc() = functionName and
  functionName.getId() = "eval"
select call, "Avoid eval(); parse or validate the input with a safer alternative."
