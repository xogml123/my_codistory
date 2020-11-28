program newton
	implicit none
    real:: f(0:10,0:10),x(0:10),ni
    integer:: i,j,k
    print *,'forward difference table(fortran)'
    data ni/4/
    data (x(i),i=0,4)/0.1,0.2,0.3,0.4,0.5/
    data (f(i,0),i=0,4)/1.302,1.616,1.954,2.328,2.750/
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
      print 440, i,x(i),(f(i,k),k=0,j)
    end do

    print*
    440 format(1x,i2,8f9.5)
end program newton