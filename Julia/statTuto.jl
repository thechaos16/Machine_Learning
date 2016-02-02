using DataFrames
using Distributions
using MultivariateStats
using GLMNet

## followings are implemented in 'MultivariateStats'
function lin_reg(X::Any,Y::Any)
	return llsq(X,Y)
end

function ridge_regression(X::Any,Y::Any,r::Real)
	return ridge(X,Y,r)
end

## use 'GLMNet'
function elastic_net(X::Any,Y::Any)
end

dsize = 10_000
dim =3
## use 'Distribution'
x = [rand(Normal(0,1),dsize),rand(Normal(3,1),dsize),rand(Normal(2,0.7),dsize)]
x = reshape(x,dsize,dim)
y = rand(Normal(5,2),dsize)

kk = lin_reg(x,y)
pp = ridge_regression(x,y,1.0)
