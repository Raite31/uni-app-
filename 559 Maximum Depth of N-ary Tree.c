#define max(a,b) ((a)>(b)?(a):(b))
int maxDepth(struct Node* root) {
    if(!root){
        return 0;
    }
    int height = 0;
    for(int i=0; i<root->numChildren; i++){
        int tmp = maxDepth(root->children[i]);
        height = max(height,tmp);
    }
    return height+1;
}

Success
Details 
Runtime: 4 ms, faster than 93.22% of C online submissions for Maximum Depth of N-ary Tree.
Memory Usage: 6.9 MB, less than 66.10% of C online submissions for Maximum Depth of N-ary Tree.