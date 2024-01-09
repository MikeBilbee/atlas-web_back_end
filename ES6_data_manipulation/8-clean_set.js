export default function cleanSet(set, startString) {
  if (!startString || startString.length < 1) {
    return '';
  }

  const setValues = Array.from(set)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length));

  return setValues.join('-');
}
