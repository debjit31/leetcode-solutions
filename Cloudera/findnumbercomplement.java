import java.util.*;
import java.lang.*;
import java.io.*;
class Test
{
    public int findComplement(int num)
    {
        int res = 0;
        int power = 1;
        while(num > 0){
            res += ((num % 2) ^ 1) * power;
            power <<= 1;
            num >>= 1;
        }
        return res;
    }
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Test s = new Test();
        int res = s.findComplement(n);
        System.out.println(res);
    }
}
