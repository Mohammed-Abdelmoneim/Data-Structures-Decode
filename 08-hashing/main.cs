using System;
using metwally;

class Program
{
    public static void Main(string[] args)
    {

        Hash hash = new Hash();
        hash.Hash32("This is Original Text");
        hash.Hash64("This is Original Text");

    }
}
