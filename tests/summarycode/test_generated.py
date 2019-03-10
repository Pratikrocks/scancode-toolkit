#
# Copyright (c) 2017 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import
from __future__ import unicode_literals

import os

from commoncode.testcase import FileBasedTesting
from scancode.cli_test_utils import check_json_scan
from scancode.cli_test_utils import run_scan_click
from summarycode import generated


class TestGeneratedCode(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_basic(self):
        expected = [
            '// This file was generated by the JavaTM Architecture '
            'for XML Binding(JAXB) Reference Implementation',
            '// Generated on: 2011.08.01 at 11:35:59 AM CEST'
        ]
        test_file = self.get_test_loc('generated/simple/generated_1.java')
        result = list(generated.get_generated_code_hint(location=test_file))
        assert expected == result

    def test_basic_alt(self):
        expected = [
            '// This file was generated by the JavaTM Architecture '
            'for XML Binding(JAXB) Reference Implementation',
            '// Generated on: 2013.11.15 at 04:17:00 PM CET'
        ]
        test_file = self.get_test_loc('generated/simple/generated_3.java')
        result = list(generated.get_generated_code_hint(location=test_file))
        assert expected == result

    def test_basic2(self):
        expected = ['* This class was generated by the JAX-WS RI.']
        test_file = self.get_test_loc('generated/simple/generated_2.java')
        result = list(generated.get_generated_code_hint(location=test_file))
        assert expected == result

    def test_basic3(self):
        expected = ['/* This class was automatically generated']
        test_file = self.get_test_loc('generated/simple/generated_4.java')
        result = list(generated.get_generated_code_hint(location=test_file))
        assert expected == result

    def test_basic4(self):
        expected = [
            '* <p>The following schema fragment specifies the '
            'expected content contained within this class.'
        ]
        test_file = self.get_test_loc('generated/simple/generated_5.java')
        result = list(generated.get_generated_code_hint(location=test_file))
        assert expected == result

    def test_basic5(self):
        expected = ['/* DO NOT EDIT THIS FILE - it is machine generated */']
        test_file = self.get_test_loc('generated/simple/generated_6.c')
        result = list(generated.get_generated_code_hint(location=test_file))
        assert expected == result

    def test_configure(self):
        expected = [
            '# Generated by GNU Autoconf 2.64 for Apache CouchDB 1.0.1.'
        ]
        test_file = self.get_test_loc('generated/simple/configure')
        result = list(generated.get_generated_code_hint(location=test_file))
        assert expected == result

    def test_tomcat_jspc(self):
        expected = [
            '<!--Automatically created by Apache Jakarta Tomcat JspC.'
        ]
        test_file = self.get_test_loc('generated/jspc/web.xml')
        result = list(generated.get_generated_code_hint(location=test_file))
        assert expected == result

    def test_generated_cli_option(self):
        test_dir = self.get_test_loc('generated/simple')
        result_file = self.get_temp_file('json')
        expected_file = self.get_test_loc('generated/cli.expected.json')
        run_scan_click(['--generated', '--json-pp', result_file, test_dir])
        check_json_scan(expected_file, result_file, remove_file_date=True, regen=False)
