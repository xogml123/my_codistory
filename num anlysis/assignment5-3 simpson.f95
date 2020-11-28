program simpson	
	implicit none
    real::z(1:10),deltasigma(1:10),sigma(1:10),sc(1:10),sctotal
    integer::R,i

    data (z(i),i=1,5)/1.5,2.5,3.5,4.5,5.5/
    data (sigma(i),i=1,5)/34.44,43.13,51.82,60.51,69.20/
    R=1
    sctotal=0
    do i=1,5
      deltasigma(i)=150*(1-1/(((R/z(i))**2+1)**(1.5)))
    end do
    do i=1,5
      sc(i)=0.16*1/1.85*log10((sigma(i)+deltasigma(i))/sigma(i))
    end do
    print *,'           i           R      sigma        deltasigma           sc'
    do i=1,5 
      print *,i,R,sigma(i),deltasigma(i),sc(i)
      sctotal=sctotal+sc(i)
    end do
    print*,'Total consolidation settlement is', sctotal


end program simpson