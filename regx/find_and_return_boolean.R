pattern_string <- "\\w \\w"
string_be_searched <- "Lee An is a famous director"

if (grepl(pattern_string, string_be_searched)) {
  print("String patter is found!")
} else {
  print("String patter is not found")
}
