program newton
	implicit none
    real:: f(0:10,0:10),x(0:10),ni
    integer:: i,j,k
    print *,'forward difference table(fortran)'
    data ni/5/
    data (x(i),i=0,5)/0.5,1.0,1.5,2.0,2.5,3.0/
    data (f(i,0),i=0,5)/1.143,1.000,0.828,0.667,0.533,0.428/
    do k=1,ni
      j=ni-k
      do i=0,j
        f(i,k)=f(i+1,k-1)-f(i,k-1)
      end do
    end do

    print*
    print*,' I    x(i)     f(i)   1st order 2nd order  ...'

    do i=0,ni
      j=ni-i
      print 440, i+1,x(i),(f(i,k),k=0,j)
    end do

   
    440 format(1x,i2,8f9.5)
    
end program newton