#
# (c) Copyright Ascensio System SIA 2022
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from plone.app.widgets.utils import get_relateditems_options
from onlyoffice.connector.interfaces import _
from onlyoffice.connector.core import formatUtils
from onlyoffice.connector.core import conversionUtils
import re

localePath = {
        'az': 'az-Latn-AZ',
        'bg': 'bg-BG',
        'cs': 'cs-CZ',
        'de': 'de-DE',
        'el': 'el-GR',
        'en-gb': 'en-GB',
        'en': 'en-US',
        'es': 'es-ES',
        'fr': 'fr-FR',
        'it': 'it-IT',
        'ja': 'ja-JP',
        'ko': 'ko-KR',
        'lv': 'lv-LV',
        'nl': 'nl-NL',
        'pl': 'pl-PL',
        'pt-br': 'pt-BR',
        'pt': 'pt-PT',
        'ru': 'ru-RU',
        'sk': 'sk-SK',
        'sv': 'sv-SE',
        'uk': 'uk-UA',
        'vi': 'vi-VN',
        'zh': 'zh-CN'
    }

def getCorrectFileName(str):
    return re.sub(r'[*?:\"<>/|\\\\]', '_', str)

def getFileNameWithoutExt(context):
    filename = context.file.filename
    ind = context.file.filename.rfind('.')
    return filename[:ind]

def getFileExt(context):
    portal_type = context.portal_type
    if  portal_type == "Image" or portal_type == "File" :
        filename = context.image.filename if portal_type == "Image" else context.file.filename

        ind = filename.rfind('.') + 1
        return filename[ind:].lower()

    return None

def getFileType(context):
    for format in formatUtils.getSupportedFormats():
        if format.name == getFileExt(context):
            return format.type

    return None

def canView(context):
    for format in formatUtils.getSupportedFormats():
        if format.name == getFileExt(context):
            return True

    return False

def canEdit(context):
    for format in formatUtils.getSupportedFormats():
        if format.name == getFileExt(context):
            return format.edit

    return False

def canFillForm(context):
    for format in formatUtils.getSupportedFormats():
        if format.name == getFileExt(context):
            return format.fillForm

    return False

def canConvert(context):
    return conversionUtils.getTargetExt(getFileExt(context)) != None

def getDefaultExtByType(str):
    if (str == 'word'):
        return 'docx'
    if (str == 'cell'):
        return 'xlsx'
    if (str == 'slide'):
        return 'pptx'
    if (str == 'form'):
        return 'docxf'

    return None

def getDefaultNameByType(str):
    if (str == 'word'):
        return _(u'Document')
    if (str == 'cell'):
        return _(u'Spreadsheet')
    if (str == 'slide'):
        return _(u'Presentation')
    if (str == 'form'):
        return _(u'Form template')

    return None

def getRelatedRtemsOptions(context):
    return get_relateditems_options(
            context=context,
            value=None,
            separator=";",
            vocabulary_name="plone.app.vocabularies.Catalog",
            vocabulary_view="@@getVocabulary",
            field_name="relatedItems",
        )