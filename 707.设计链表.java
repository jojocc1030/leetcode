/*
 * @lc app=leetcode.cn id=707 lang=java
 *
 * [707] 设计链表
 */

// @lc code=start
class ListNode{
    int val;
    ListNode next;

    ListNode(){

    }

    ListNode(int val){
        this.val = val;
    }

    ListNode(ListNode next, int val){
        this.next = next;
        this.val = val;
    }
}


class MyLinkedList {
    ListNode dummyhead;
    int size;

    public MyLinkedList() {
        size = 0;
        dummyhead = new ListNode(-1); //设置虚拟头节点
    }
    
    public int get(int index) {
        if(index >= size || index < 0) return -1;

        ListNode cur = dummyhead;
        for(int i = -1; i < index; i ++){
            cur = cur.next;
        }
        return cur.val;
        
    }
    
    public void addAtHead(int val) {
        addAtIndex(0, val);

    }
    
    public void addAtTail(int val) {
        addAtIndex(size, val); 
    }
    
    public void addAtIndex(int index, int val) {
        if(index > size || index < 0) return;
    
        ListNode newNode = new ListNode(val);
        ListNode cur = dummyhead;
        for(int i = -1; i < index - 1; i ++){
            cur = cur.next;
        }
        newNode.next = cur.next;
        cur.next = newNode;
        size ++;

    }
    
    public void deleteAtIndex(int index) {
        if(index >= size || index < 0) return;
        ListNode pre = dummyhead;
        for(int i = -1; i < index - 1; i ++){
            pre = pre.next;
        }
        pre.next = pre.next.next;
        size --;


    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
// @lc code=end

