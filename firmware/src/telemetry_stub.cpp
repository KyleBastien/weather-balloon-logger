#include "../include/telemetry.h"

#include <stdio.h>

namespace weather_balloon {
namespace telemetry {

bool format_sample(char* output, size_t capacity) {
  if (output == nullptr || capacity == 0) {
    return false;
  }
  // Happy-path placeholder: sequence, GPS-fix flag, altitude, logger state.
  const int written = snprintf(output, capacity, "0,0,0,READY");
  return written > 0 && static_cast<size_t>(written) < capacity;
}

}  // namespace telemetry
}  // namespace weather_balloon
