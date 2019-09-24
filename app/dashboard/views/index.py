# Copyright (C) Linaro Limited 2014,2017,2019
# Author: Matt Hart <matthew.hart@linaro.org>
# Author: Milo Casagrande <milo.casagrande@linaro.org>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

from flask import (
    current_app as app,
    render_template
)
from flask.views import View


class IndexView(View):

    PAGE_TITLE = app.config.get("DEFAULT_PAGE_TITLE")
    INDEX_TITLE = "%s &mdash; %s" % (PAGE_TITLE, "Home")

    def dispatch_request(self, *args, **kwargs):
        return render_template("index.html", page_title=self.INDEX_TITLE)
