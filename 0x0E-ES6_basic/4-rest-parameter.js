export default function returnHowManyArguments(...theArgs) {
  return arguments.length + theArgs.length;
}
