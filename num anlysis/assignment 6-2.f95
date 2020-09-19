program gauss_eli
	implicit none
    real :: a(50,50),c,temp,soln(50),factor
    integer :: pivot,s,n,n2,k,p,o,i,j,row,col,a_i,a_j,rmax

    print *, "How much is Matrix's size? i,j"
    read *,a_i,a_j
    n=a_i
    n2=a_j
    do p=1,a_i
      do o=1,a_j
        print *,"a<<<",p,",",o,">>> = ?"
        read *,c
        a(p,o)=c
      end do
    end do
    
      do pivot=1,n-1
        rmax=pivot
        do row=pivot,a_i
          if(ABS(a(rmax,pivot))<abs(a(row,pivot))) then
            rmax=row
          end if
        end do
        if(rmax /= pivot) then
          do k=1,a_j
            temp=a(rmax,k)
            a(rmax,k)=a(pivot,k)
            a(pivot,k)=temp
          end do
        end if
        !elimination
        do row=pivot+1,n
          factor=a(row,pivot)/a(pivot,pivot)
          do col=1,n2
            a(row,col)=a(row,col)-a(pivot,col)*factor
          end do
        end do
      end do
    
    !back subtitution
  do i=1,n2-n
    do k=1,n
      a(k,n+1)=a(k,n+i)
    end do
      
    soln=0
    do o=n,1,-1
      do p=n+1,o,-1
        a(o,n+1)=a(o,n+1)-soln(p)*a(o,p)
      end do
      soln(o)=a(o,n+1)/a(o,o)
    end do
    print *,i,'th solution'
    do j=1,n
      
      print *,soln(j)
    end do
  end do
    


end program gauss_eli
