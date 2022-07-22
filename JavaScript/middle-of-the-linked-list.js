var middleNode = function(head) {
  let middle = head;
  let end = head;
  while (end) {
    if (end.next === null) {
      break;
    } else {
      end = end.next.next;
    }
    middle = middle.next;
  }
  return middle;
};