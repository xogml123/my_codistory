program simpson	
	implicit none
    real:: h,x(0:100),func(0:100),s,r,A,B,ss
    integer:: N,i,w,LS
    open(unit=30, file='assignment2.txt', status='unknown')
    
3   print *,"How many Sections do you want to calculate with?"
	read *, N
    
    ss=0    
    s=0      
    LS=0     
    
	
    do i=0,4*N !h=0.4
      read (30,*) x(i),func(i)
    end do
    
    
    A=x(0)
    B=x(4*N)
    h=(B-A)/N
    
    do i=0,N
	  
      w=4
      
      if(i==0 .or. i==N) then
        w=1
      end if
      s=s+w*func(4*i) !h-0.2
    end do
    s=s*h/3
    print *, "Results =",s
 
        
      
end program simpson