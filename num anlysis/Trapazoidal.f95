program trapazoidal
	implicit none
    real:: h,x,s,r,A,B
    integer:: N,i,w
3   print *,"How many Sections do you want to calculate with?"
	read *, N
    print*,"what's the starting section?"
    read*, A
    print *,"what's the ending section?"
    read *, B
    h=(B-A)/N

    s=0
    do i=0,N
      x=A+h*i
      w=2
      if (i==0 .or. i==N)then
        w=1
      end if
      s=s+w*(1+(x/2)**2)
      print *, I,x,h,w
    end do

      s=s*h/2
      print *, 'Result is ',s

    
end program trapazoidal