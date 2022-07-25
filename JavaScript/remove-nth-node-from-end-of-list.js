/* eslint-disable no-undef */
var removeNthFromEnd = function(head, n) {
  let dummyHead = new ListNode(-1);
  dummyHead.next = head;
  let result = dummyHead;
  let tail = head;
  
  while (n--) {
    tail = tail.next;
  }
  
  let curr = head;
  let prev = dummyHead;
  while (tail) {
    tail = tail.next;
    curr = curr.next;
    prev = prev.next;
  }
  
  prev.next = curr.next;
  return result.next;
};