using System;
using metwally;

class Program
{
    public static void Main(string[] args)
    {
    
        BinaryTree<int> tree = new BinaryTree<int>();
        //tree.BSInsert(1);
        //tree.BSInsert(4);
        //tree.BSInsert(2);
        //tree.BSInsert(3);
        //tree.BSInsert(6);
        //tree.BSInsert(5);
        //tree.Print();

        //Console.WriteLine(tree.IsExsit(8));
        
        //tree.InOrder();

        //tree.BSInsert(4);
        //tree.BSInsert(6);
        //tree.BSInsert(7);
        //tree.BSInsert(5);
        //tree.BSInsert(2);
        //tree.BSInsert(1);
        //tree.BSInsert(3);
        //tree.Print();

        //tree.BsDelete(4);
        //tree.Print();
        //tree.BsDelete(6);
        //tree.Print();
        //tree.BsDelete(3);
        //tree.BsDelete(5);
        //tree.Print();
        //tree.BsDelete(7);
        //tree.Print();
        //tree.BsDelete(2);
        //tree.Print();
        //tree.BsDelete(1);
        //tree.Print();
        
        tree.BSInsert(1);
        tree.BSInsert(2);
        tree.BSInsert(3);
        tree.BSInsert(4);
        tree.BSInsert(5);
        tree.BSInsert(6);
        tree.BSInsert(7);
        tree.Print();

        tree.Balance();
        tree.Print();

        
        
        
        // BinaryTree<char> tree = new BinaryTree<char>();
        // tree.Insert('A');
        // tree.Insert('B');
        // tree.Insert('C');
        // tree.Insert('D');
        // tree.Insert('E');
        // tree.Insert('F');
        // tree.Insert('G');
        // tree.Insert('H');
        // tree.Insert('I');
        // tree.Print();
        
        // Console.WriteLine("Height: " + tree.Height());
        // tree.PreOrder();
        // tree.InOrder();
        // tree.PostOrder();

    }
}
