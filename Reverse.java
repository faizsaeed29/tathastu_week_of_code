//Reverse of Array

import java.util.*;
class Reverse
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of array:");
        int n = sc.nextInt();

        int a[] = new int[n];
        for(int i=0;i<n;i++)
        {
            a[i] = sc.nextInt();
        }

        reverseArray(a);

        printArray(a);
    }

    public static void reverseArray(int arr[])
    {
        int start,end,temp;
        for(start =0,end=arr.length-1;start<end;start++,end--)
        {
            temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
        }
    }

    public static void printArray(int a[])
    {
        for(int i=0;i<a.length;i++)
        {
            System.out.print("\t"+a[i]);
        }
    }
}