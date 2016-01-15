using DataFrames
using Distributions
using MultivariateStats

function linReg(X::Any,Y::Any)
	return llsq(X,Y)
end

dsize = 10_000
dim =3
x = [rand(Normal(0,1),dsize),rand(Normal(3,1),dsize),rand(Normal(2,0.7),dsize)]
x = reshape(x,dsize,dim)
y = rand(Normal(5,2),dsize)

kk = linReg(x,y)
