from tkinter.tix import ListNoteBook
from typing import Optional

def hasCycle(self, head: Optional[ListNoteBook]) -> bool:
  if not head:
    return False
    
  fast, slow = head, head
  while fast.next and fast.next.next:
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
      return True
  return False