class LRUCache {
public:
    class Node{
        public:
        int key;
        int val;
        Node* next;
        Node* prev;

        Node(int k, int v){
            this->key = k;
            this->val = v;
        }
    };

    Node* head = new Node(-1, -1);
    Node* tail = new Node(-1, -1);
    int cap;
    unordered_map<int, Node*> m;

    LRUCache(int capacity) {
        cap = capacity;
        head->next = tail;
        tail->prev = head;
    }

    // add at the last
    void addNode(Node* newNode){
        Node* temp = head->next;
        newNode->next = temp;
        newNode->prev = head;

        head->next = newNode;
        temp->prev = newNode;
    }

    // removing last used
    void deleteNode(Node * delNode){
        Node* prevv = delNode->prev;
        Node* nextt = delNode->next;

        prevv ->next = nextt;
        nextt->prev = prevv;

    }

    
    int get(int key) {
        if(m.find(key) != m.end()){
            Node* resNode = m[key];
            int ans = resNode->val;

            m.erase(key);
            deleteNode(resNode);
            addNode(resNode);

            m[key] = head->next;
            return ans;
        }
        return -1;
    }
    
    void put(int key, int value) {
       if(m.find(key) != m.end()){
           Node* curr = m[key];
           m.erase(key);
           deleteNode(curr);
       }

       if(m.size() == cap){
           m.erase(tail->prev ->key);
           deleteNode(tail->prev);
       }

       addNode(new Node(key, value));
       m[key] = head->next;

    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */