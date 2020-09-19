export default function iterateThroughObject(reportWithIterator) {
  return reportWithIterator.join(' | ');
}

console.log(iterateThroughObject([ 'B', 'o', 'b' ]));