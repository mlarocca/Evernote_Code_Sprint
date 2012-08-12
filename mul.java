import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class mul {
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String inputLine;
		int N;		//Number of input elements to expect from the input
		int i, zeros_counter = 0;

		inputLine = in.readLine();
		N = Integer.parseInt(inputLine);

		
		long[] A = new long[N];
		long mul = 1;
		//Read input array, computing the cumulative product and counting the number of zeros
		for (i=0; i<N; i++){
			inputLine = in.readLine();
			A[i] = Integer.parseInt(inputLine);	            
            if (A[i]==0){
            	zeros_counter += 1;
            }else{
				mul *= A[i];
            }
		}
		
	    switch(zeros_counter){
	        case 0:	
	        	//No zeros in the input: every resulting element is the product of the
	        	//remaining ones, i.e. every element is the cumulative product of 
	        	//the array over the element itself.
	            for (i=0; i<N; i++){		
	                A[i] = mul / A[i];
	                System.out.println(A[i]);
	            }        
	            break;
	        
	        case 1:
	        	//Exactly one zeros: every output element is zero but the one corresponding
	        	//to the zero input number, which is the cumulative product of the remaining
	        	//elements.
	            for (i=0; i<N; i++){
				if (A[i]==0){
						System.out.println(mul);
	                }else{ 
	                	System.out.println(0);
	                }
	            }        
	            break;
	        
	        default:
	        	//More than one zero: every output element multiply a zero, so
	        	//every output element is zero.
	            for (i=0; i<N; i++){
	            	System.out.println(0);
	            }                   
	    }
	}
}
