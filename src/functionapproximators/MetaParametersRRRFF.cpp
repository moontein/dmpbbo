/**
 * @file   MetaParametersRRRFF.cpp
 * @brief  MetaParametersRRRFF class source file.
 * @author Freek Stulp, Thibaut Munzer
 *
 * This file is part of DmpBbo, a set of libraries and programs for the 
 * black-box optimization of dynamical movement primitives.
 * Copyright (C) 2014 Freek Stulp, ENSTA-ParisTech
 * 
 * DmpBbo is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 * 
 * DmpBbo is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public License
 * along with DmpBbo.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <boost/serialization/export.hpp>
#include <boost/archive/text_iarchive.hpp>
#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/xml_iarchive.hpp>
#include <boost/archive/xml_oarchive.hpp>
#include "functionapproximators/MetaParametersRRRFF.hpp"

/** For boost::serialization. See http://www.boost.org/doc/libs/1_55_0/libs/serialization/doc/special.html#export */
BOOST_CLASS_EXPORT_IMPLEMENT(DmpBbo::MetaParametersRRRFF);

#include "dmpbbo_io/EigenBoostSerialization.hpp"
#include "dmpbbo_io/BoostSerializationToString.hpp"

#include <iostream>


using namespace std;

namespace DmpBbo {

MetaParametersRRRFF::MetaParametersRRRFF(int expected_input_dim, int number_of_basis_functions, double regularization, double gamma) 
	:
    MetaParameters(expected_input_dim),
    number_of_basis_functions_(number_of_basis_functions),
    regularization_(regularization),
    gamma_(gamma)
{
}
		
MetaParametersRRRFF* MetaParametersRRRFF::clone(void) const 
{
  return new MetaParametersRRRFF(getExpectedInputDim(),number_of_basis_functions_,regularization_,gamma_);
}

template<class Archive>
void MetaParametersRRRFF::serialize(Archive & ar, const unsigned int version)
{
  // serialize base class information
  ar & BOOST_SERIALIZATION_BASE_OBJECT_NVP(MetaParameters);

  ar & BOOST_SERIALIZATION_NVP(number_of_basis_functions_);
  ar & BOOST_SERIALIZATION_NVP(regularization_);
  ar & BOOST_SERIALIZATION_NVP(gamma_);
}

string MetaParametersRRRFF::toString(void) const 
{
  RETURN_STRING_FROM_BOOST_SERIALIZATION_XML("MetaParametersRRRFF");
}

}
