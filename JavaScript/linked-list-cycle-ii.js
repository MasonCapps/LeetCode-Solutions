var detectCycle = function(head) {
  if (!head) {
    return null;
  } else if (!head.next) {
    return null;
  }
  
  let fast = head;
  let slow = head;
  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow.next;
    if (fast === slow) {
      break;
    }
  }
  if (fast !== slow) {
    return null;
  }
  
  let connectFinder = head;
  while (connectFinder !== slow) {
    slow = slow.next;
    connectFinder = connectFinder.next;
  }
  return connectFinder;
};