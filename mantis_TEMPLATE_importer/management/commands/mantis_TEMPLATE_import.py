# Copyright (c) Siemens AG, 2013
#
# This file is part of MANTIS.  MANTIS is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either version 2
# of the License, or(at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#


from dingos.importer import DingoImportCommand

from mantis_TEMPLATE_importer.importer import TEMPLATE_Import

class Command(DingoImportCommand):
    """
    This class implements the command for importing TEMPLATE_Import
    files into DINGO.
    """

    Importer = TEMPLATE_Import()

    # below works for mantis 0.3.0 and above
    Importer_Class = TEMPLATE_Import

    help = 'Imports TEMPLATE XML files of specified paths into DINGO'

