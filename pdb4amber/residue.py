# Romain M. Wolf, NIBR Basel, December 2013
# with revisions by Pawel Janowski & Jason Swails, Rutgers U., Feb. 2014
#    & Jan. 2015

#  Copyright (c) 2013, Novartis Institutes for BioMedical Research Inc.
#  All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#     * Neither the name of Novartis Institutes for BioMedical Research Inc.
#       nor the names of its contributors may be used to endorse or promote
#       products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

__all__ = [
    'RESPROT', 'RESNA', 'RESSOLV', 'RESSUGAR', 'AMBER_SUPPORTED_RESNAMES'
]

# 
HEAVY_ATOM_DICT = {
    'ALA': 5,
    'ARG': 11,
    'ASN': 8,
    'ASP': 8,
    'CYS': 6,
    'GLN': 9,
    'GLU': 9,
    'GLY': 4,
    'HIS': 10,
    'ILE': 8,
    'LEU': 8,
    'LYS': 9,
    'MET': 8,
    'PHE': 11,
    'PRO': 7,
    'SER': 6,
    'THR': 7,
    'TRP': 14,
    'TYR': 12,
    'VAL': 7,
    'HID': 10,
    'HIE': 10,
    'HIN': 10,
    'HIP': 10,
    'CYX': 6,
    'ASH': 8,
    'GLH': 9,
    'LYH': 9,
    'CYM': 6
}

# Global constants
RESPROT = ('ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS',
           'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP',
           'TYR', 'VAL', 'HID', 'HIE', 'HIN', 'HIP', 'CYX', 'ASH', 'GLH',
           'LYH', 'ACE', 'NME', 'GL4', 'AS4', 'CYM')

RESNA = ('C', 'G', 'U', 'A', 'DC', 'DG', 'DT', 'DA', 'OHE' )

RESSOLV = ('WAT', 'HOH', 'AG', 'AL', 'Ag', 'BA', 'BR', 'Be', 'CA', 'CD', 'CE',
           'CL', 'CO', 'CR', 'CS', 'CU', 'CU1', 'Ce', 'Cl-', 'Cr', 'Dy', 'EU',
           'EU3', 'Er', 'F', 'FE', 'FE2', 'GD3', 'HE+', 'HG', 'HZ+', 'Hf',
           'IN', 'IOD', 'K', 'K+', 'LA', 'LI', 'LU', 'MG', 'MN', 'NA', 'NH4',
           'NI', 'Na+', 'Nd', 'PB', 'PD', 'PR', 'PT', 'Pu', 'RB', 'Ra', 'SM',
           'SR', 'Sm', 'Sn', 'TB', 'TL', 'Th', 'Tl', 'Tm', 'U4+', 'V2+', 'Y',
           'YB2', 'ZN', 'Zr')

#  Following not used right now; probably needs an flag to indicate that
#    we expect sugar residues in the input pdb file.)

RESSUGAR = (
    '0AA', '0AB', '0AD', '0AU', '0BA', '0BB', '0BC', '0BD', '0BU', '0CA',
    '0CB', '0CD', '0CU', '0DA', '0DB', '0DD', '0DU', '0EA', '0EB', '0FA',
    '0FB', '0GA', '0GB', '0GL', '0HA', '0HB', '0JA', '0JB', '0JD', '0JU',
    '0KA', '0KB', '0LA', '0LB', '0MA', '0MB', '0NA', '0NB', '0OA', '0OB',
    '0PA', '0PB', '0PD', '0PU', '0QA', '0QB', '0RA', '0RB', '0RD', '0RU',
    '0SA', '0SB', '0TA', '0TB', '0TV', '0Tv', '0UA', '0UB', '0VA', '0VB',
    '0WA', '0WB', '0XA', '0XB', '0XD', '0XU', '0YA', '0YB', '0ZA', '0ZB',
    '0aA', '0aB', '0aD', '0aU', '0bA', '0bB', '0bC', '0bD', '0bU', '0cA',
    '0cB', '0cD', '0cU', '0dA', '0dB', '0dD', '0dU', '0eA', '0eB', '0fA',
    '0fB', '0gA', '0gB', '0gL', '0hA', '0hB', '0jA', '0jB', '0jD', '0jU',
    '0kA', '0kB', '0lA', '0lB', '0mA', '0mB', '0nA', '0nB', '0oA', '0oB',
    '0pA', '0pB', '0pD', '0pU', '0qA', '0qB', '0rA', '0rB', '0rD', '0rU',
    '0sA', '0sB', '0tA', '0tB', '0tV', '0tv', '0uA', '0uB', '0vA', '0vB',
    '0wA', '0wB', '0xA', '0xB', '0xD', '0xU', '0yA', '0yB', '0zA', '0zB',
    '1AA', '1AB', '1AD', '1AU', '1BA', '1BB', '1BD', '1BU', '1CA', '1CB',
    '1CD', '1CU', '1DA', '1DB', '1DD', '1DU', '1EA', '1EB', '1FA', '1FB',
    '1GA', '1GB', '1HA', '1HB', '1JA', '1JB', '1JD', '1JU', '1KA', '1KB',
    '1LA', '1LB', '1MA', '1MB', '1NA', '1NB', '1OA', '1OB', '1PA', '1PB',
    '1PD', '1PU', '1QA', '1QB', '1RA', '1RB', '1RD', '1RU', '1TA', '1TB',
    '1TV', '1Tv', '1UA', '1UB', '1VA', '1VB', '1WA', '1WB', '1XA', '1XB',
    '1XD', '1XU', '1YA', '1YB', '1ZA', '1ZB', '1aA', '1aB', '1aD', '1aU',
    '1bA', '1bB', '1bD', '1bU', '1cA', '1cB', '1cD', '1cU', '1dA', '1dB',
    '1dD', '1dU', '1eA', '1eB', '1fA', '1fB', '1gA', '1gB', '1hA', '1hB',
    '1jA', '1jB', '1jD', '1jU', '1kA', '1kB', '1lA', '1lB', '1mA', '1mB',
    '1nA', '1nB', '1oA', '1oB', '1pA', '1pB', '1pD', '1pU', '1qA', '1qB',
    '1rA', '1rB', '1rD', '1rU', '1tA', '1tB', '1tV', '1tv', '1uA', '1uB',
    '1vA', '1vB', '1wA', '1wB', '1xA', '1xB', '1xD', '1xU', '1yA', '1yB',
    '1zA', '1zB', '2AA', '2AB', '2AD', '2AU', '2BA', '2BB', '2BD', '2BU',
    '2CA', '2CB', '2CD', '2CU', '2DA', '2DB', '2DD', '2DU', '2EA', '2EB',
    '2FA', '2FB', '2GA', '2GB', '2HA', '2HB', '2JA', '2JB', '2JD', '2JU',
    '2KA', '2KB', '2LA', '2LB', '2MA', '2MB', '2NA', '2NB', '2OA', '2OB',
    '2PA', '2PB', '2PD', '2PU', '2QA', '2QB', '2RA', '2RB', '2RD', '2RU',
    '2TA', '2TB', '2TV', '2Tv', '2UA', '2UB', '2XA', '2XB', '2XD', '2XU',
    '2ZA', '2ZB', '2aA', '2aB', '2aD', '2aU', '2bA', '2bB', '2bD', '2bU',
    '2cA', '2cB', '2cD', '2cU', '2dA', '2dB', '2dD', '2dU', '2eA', '2eB',
    '2fA', '2fB', '2gA', '2gB', '2hA', '2hB', '2jA', '2jB', '2jD', '2jU',
    '2kA', '2kB', '2lA', '2lB', '2mA', '2mB', '2nA', '2nB', '2oA', '2oB',
    '2pA', '2pB', '2pD', '2pU', '2qA', '2qB', '2rA', '2rB', '2rD', '2rU',
    '2tA', '2tB', '2tV', '2tv', '2uA', '2uB', '2xA', '2xB', '2xD', '2xU',
    '2zA', '2zB', '3AA', '3AB', '3AD', '3AU', '3BA', '3BB', '3BC', '3BD',
    '3BU', '3CA', '3CB', '3CD', '3CU', '3DA', '3DB', '3DD', '3DU', '3EA',
    '3EB', '3FA', '3FB', '3GA', '3GB', '3HA', '3HB', '3JA', '3JB', '3JD',
    '3JU', '3KA', '3KB', '3LA', '3LB', '3MA', '3MB', '3NA', '3NB', '3OA',
    '3OB', '3PA', '3PB', '3PD', '3PU', '3QA', '3QB', '3RA', '3RB', '3RD',
    '3RU', '3TA', '3TB', '3UA', '3UB', '3VA', '3VB', '3WA', '3WB', '3XA',
    '3XB', '3XD', '3XU', '3YA', '3YB', '3ZA', '3ZB', '3aA', '3aB', '3aD',
    '3aU', '3bA', '3bB', '3bC', '3bD', '3bU', '3cA', '3cB', '3cD', '3cU',
    '3dA', '3dB', '3dD', '3dU', '3eA', '3eB', '3fA', '3fB', '3gA', '3gB',
    '3hA', '3hB', '3jA', '3jB', '3jD', '3jU', '3kA', '3kB', '3lA', '3lB',
    '3mA', '3mB', '3nA', '3nB', '3oA', '3oB', '3pA', '3pB', '3pD', '3pU',
    '3qA', '3qB', '3rA', '3rB', '3rD', '3rU', '3tA', '3tB', '3uA', '3uB',
    '3vA', '3vB', '3wA', '3wB', '3xA', '3xB', '3xD', '3xU', '3yA', '3yB',
    '3zA', '3zB', '4AA', '4AB', '4BA', '4BB', '4BD', '4BU', '4CA', '4CB',
    '4CD', '4CU', '4DA', '4DB', '4EA', '4EB', '4FA', '4FB', '4GA', '4GB',
    '4GL', '4HA', '4HB', '4JA', '4JB', '4JD', '4JU', '4KA', '4KB', '4LA',
    '4LB', '4MA', '4MB', '4NA', '4NB', '4OA', '4OB', '4PA', '4PB', '4PD',
    '4PU', '4QA', '4QB', '4RA', '4RB', '4SA', '4SB', '4TA', '4TB', '4TV',
    '4Tv', '4UA', '4UB', '4VA', '4VB', '4WA', '4WB', '4XA', '4XB', '4YA',
    '4YB', '4ZA', '4ZB', '4aA', '4aB', '4bA', '4bB', '4bD', '4bU', '4cA',
    '4cB', '4cD', '4cU', '4dA', '4dB', '4eA', '4eB', '4fA', '4fB', '4gA',
    '4gB', '4gL', '4hA', '4hB', '4jA', '4jB', '4jD', '4jU', '4kA', '4kB',
    '4lA', '4lB', '4mA', '4mB', '4nA', '4nB', '4oA', '4oB', '4pA', '4pB',
    '4pD', '4pU', '4qA', '4qB', '4rA', '4rB', '4sA', '4sB', '4tA', '4tB',
    '4tV', '4tv', '4uA', '4uB', '4vA', '4vB', '4wA', '4wB', '4xA', '4xB',
    '4yA', '4yB', '4zA', '4zB', '5AD', '5AU', '5BA', '5BB', '5CA', '5CB',
    '5DD', '5DU', '5JA', '5JB', '5PA', '5PB', '5RD', '5RU', '5XD', '5XU',
    '5aD', '5aU', '5bA', '5bB', '5cA', '5cB', '5dD', '5dU', '5jA', '5jB',
    '5pA', '5pB', '5rD', '5rU', '5xD', '5xU', '6BD', '6BU', '6CD', '6CU',
    '6EA', '6EB', '6GA', '6GB', '6JD', '6JU', '6KA', '6KB', '6LA', '6LB',
    '6MA', '6MB', '6NA', '6NB', '6PD', '6PU', '6TA', '6TB', '6VA', '6VB',
    '6WA', '6WB', '6YA', '6YB', '6bD', '6bU', '6cD', '6cU', '6eA', '6eB',
    '6gA', '6gB', '6jD', '6jU', '6kA', '6kB', '6lA', '6lB', '6mA', '6mB',
    '6nA', '6nB', '6pD', '6pU', '6tA', '6tB', '6vA', '6vB', '6wA', '6wB',
    '6yA', '6yB', '7GL', '7SA', '7SB', '7gL', '7sA', '7sB', '8GL', '8SA',
    '8SB', '8gL', '8sA', '8sB', '9GL', '9SA', '9SB', '9gL', '9sA', '9sB',
    'ACX', 'AGL', 'ASA', 'ASB', 'AgL', 'AsA', 'AsB', 'BGL', 'BSA', 'BSB',
    'BgL', 'BsA', 'BsB', 'CA2', 'CGL', 'CSA', 'CSB', 'CgL', 'CsA', 'CsB',
    'DGL', 'DSA', 'DSB', 'DgL', 'DsA', 'DsB', 'EGL', 'ESA', 'ESB', 'EgL',
    'EsA', 'EsB', 'FGL', 'FSA', 'FSB', 'FgL', 'FsA', 'FsB', 'GGL', 'GSA',
    'GSB', 'GgL', 'GsA', 'GsB', 'HGL', 'HSA', 'HSB', 'HgL', 'HsA', 'HsB',
    'IGL', 'ISA', 'ISB', 'IgL', 'IsA', 'IsB', 'JGL', 'JSA', 'JSB', 'JgL',
    'JsA', 'JsB', 'KGL', 'KSA', 'KSB', 'KgL', 'KsA', 'KsB', 'MEX', 'NLN',
    'OLS', 'OLT', 'OME', 'PEA', 'PEB', 'PGA', 'PGB', 'PKA', 'PKB', 'PLA',
    'PLB', 'PMA', 'PMB', 'PNA', 'PNB', 'PTA', 'PTB', 'PeA', 'PeB', 'PgA',
    'PgB', 'PkA', 'PkB', 'PlA', 'PlB', 'PmA', 'PmB', 'PnA', 'PnB', 'PtA',
    'PtB', 'QBD', 'QBU', 'QCD', 'QCU', 'QEA', 'QEB', 'QGA', 'QGB', 'QJD',
    'QJU', 'QKA', 'QKB', 'QLA', 'QLB', 'QMA', 'QMB', 'QNA', 'QNB', 'QPD',
    'QPU', 'QTA', 'QTB', 'QVA', 'QVB', 'QWA', 'QWB', 'QYA', 'QYB', 'QbD',
    'QbU', 'QcD', 'QcU', 'QeA', 'QeB', 'QgA', 'QgB', 'QjD', 'QjU', 'QkA',
    'QkB', 'QlA', 'QlB', 'QmA', 'QmB', 'QnA', 'QnB', 'QpD', 'QpU', 'QtA',
    'QtB', 'QvA', 'QvB', 'QwA', 'QwB', 'QyA', 'QyB', 'REA', 'REB', 'RGA',
    'RGB', 'RKA', 'RKB', 'RLA', 'RLB', 'RMA', 'RMB', 'RNA', 'RNB', 'ROH',
    'RTA', 'RTB', 'ReA', 'ReB', 'RgA', 'RgB', 'RkA', 'RkB', 'RlA', 'RlB',
    'RmA', 'RmB', 'RnA', 'RnB', 'RtA', 'RtB', 'SEA', 'SEB', 'SGA', 'SGB',
    'SKA', 'SKB', 'SLA', 'SLB', 'SMA', 'SMB', 'SNA', 'SNB', 'STA', 'STB',
    'SO3', 'SeA', 'SeB', 'SgA', 'SgB', 'SkA', 'SkB', 'SlA', 'SlB', 'SmA',
    'SmB', 'SnA', 'SnB', 'StA', 'StB', 'TAA', 'TAB', 'TBT', 'TDA', 'TDB',
    'TEA', 'TEB', 'TFA', 'TFB', 'TGA', 'TGB', 'THA', 'THB', 'TKA', 'TKB',
    'TLA', 'TLB', 'TMA', 'TMB', 'TNA', 'TNB', 'TOA', 'TOB', 'TQA', 'TQB',
    'TRA', 'TRB', 'TTA', 'TTB', 'TUA', 'TUB', 'TXA', 'TXB', 'TZA', 'TZB',
    'TaA', 'TaB', 'TdA', 'TdB', 'TeA', 'TeB', 'TfA', 'TfB', 'TgA', 'TgB',
    'ThA', 'ThB', 'TkA', 'TkB', 'TlA', 'TlB', 'TmA', 'TmB', 'TnA', 'TnB',
    'ToA', 'ToB', 'TqA', 'TqB', 'TrA', 'TrB', 'TtA', 'TtB', 'TuA', 'TuB',
    'TxA', 'TxB', 'TzA', 'TzB', 'UBD', 'UBU', 'UCD', 'UCU', 'UEA', 'UEB',
    'UGA', 'UGB', 'UJD', 'UJU', 'UKA', 'UKB', 'ULA', 'ULB', 'UMA', 'UMB',
    'UNA', 'UNB', 'UPD', 'UPU', 'UTA', 'UTB', 'UVA', 'UVB', 'UWA', 'UWB',
    'UYA', 'UYB', 'UbD', 'UbU', 'UcD', 'UcU', 'UeA', 'UeB', 'UgA', 'UgB',
    'UjD', 'UjU', 'UkA', 'UkB', 'UlA', 'UlB', 'UmA', 'UmB', 'UnA', 'UnB',
    'UpD', 'UpU', 'UtA', 'UtB', 'UvA', 'UvB', 'UwA', 'UwB', 'UyA', 'UyB',
    'VBD', 'VBU', 'VCD', 'VCU', 'VEA', 'VEB', 'VGA', 'VGB', 'VJD', 'VJU',
    'VKA', 'VKB', 'VLA', 'VLB', 'VMA', 'VMB', 'VNA', 'VNB', 'VPD', 'VPU',
    'VTA', 'VTB', 'VVA', 'VVB', 'VWA', 'VWB', 'VYA', 'VYB', 'VbD', 'VbU',
    'VcD', 'VcU', 'VeA', 'VeB', 'VgA', 'VgB', 'VjD', 'VjU', 'VkA', 'VkB',
    'VlA', 'VlB', 'VmA', 'VmB', 'VnA', 'VnB', 'VpD', 'VpU', 'VtA', 'VtB',
    'VvA', 'VvB', 'VwA', 'VwB', 'VyA', 'VyB', 'WAA', 'WAB', 'WBA', 'WBB',
    'WBD', 'WBU', 'WCA', 'WCB', 'WCD', 'WCU', 'WDA', 'WDB', 'WEA', 'WEB',
    'WFA', 'WFB', 'WGA', 'WGB', 'WHA', 'WHB', 'WJA', 'WJB', 'WJD', 'WJU',
    'WKA', 'WKB', 'WLA', 'WLB', 'WMA', 'WMB', 'WNA', 'WNB', 'WOA', 'WOB',
    'WPA', 'WPB', 'WPD', 'WPU', 'WQA', 'WQB', 'WRA', 'WRB', 'WTA', 'WTB',
    'WUA', 'WUB', 'WVA', 'WVB', 'WWA', 'WWB', 'WXA', 'WXB', 'WYA', 'WYB',
    'WZA', 'WZB', 'WaA', 'WaB', 'WbA', 'WbB', 'WbD', 'WbU', 'WcA', 'WcB',
    'WcD', 'WcU', 'WdA', 'WdB', 'WeA', 'WeB', 'WfA', 'WfB', 'WgA', 'WgB',
    'WhA', 'WhB', 'WjA', 'WjB', 'WjD', 'WjU', 'WkA', 'WkB', 'WlA', 'WlB',
    'WmA', 'WmB', 'WnA', 'WnB', 'WoA', 'WoB', 'WpA', 'WpB', 'WpD', 'WpU',
    'WqA', 'WqB', 'WrA', 'WrB', 'WtA', 'WtB', 'WuA', 'WuB', 'WvA', 'WvB',
    'WwA', 'WwB', 'WxA', 'WxB', 'WyA', 'WyB', 'WzA', 'WzB', 'XEA', 'XEB',
    'XGA', 'XGB', 'XKA', 'XKB', 'XLA', 'XLB', 'XMA', 'XMB', 'XNA', 'XNB',
    'XTA', 'XTB', 'XeA', 'XeB', 'XgA', 'XgB', 'XkA', 'XkB', 'XlA', 'XlB',
    'XmA', 'XmB', 'XnA', 'XnB', 'XtA', 'XtB', 'YAA', 'YAB', 'YDA', 'YDB',
    'YEA', 'YEB', 'YFA', 'YFB', 'YGA', 'YGB', 'YHA', 'YHB', 'YKA', 'YKB',
    'YLA', 'YLB', 'YMA', 'YMB', 'YNA', 'YNB', 'YOA', 'YOB', 'YQA', 'YQB',
    'YRA', 'YRB', 'YTA', 'YTB', 'YTV', 'YTv', 'YUA', 'YUB', 'YXA', 'YXB',
    'YZA', 'YZB', 'YaA', 'YaB', 'YdA', 'YdB', 'YeA', 'YeB', 'YfA', 'YfB',
    'YgA', 'YgB', 'YhA', 'YhB', 'YkA', 'YkB', 'YlA', 'YlB', 'YmA', 'YmB',
    'YnA', 'YnB', 'YoA', 'YoB', 'YqA', 'YqB', 'YrA', 'YrB', 'YtA', 'YtB',
    'YtV', 'Ytv', 'YuA', 'YuB', 'YxA', 'YxB', 'YzA', 'YzB', 'ZAA', 'ZAB',
    'ZAD', 'ZAU', 'ZDA', 'ZDB', 'ZDD', 'ZDU', 'ZEA', 'ZEB', 'ZFA', 'ZFB',
    'ZGA', 'ZGB', 'ZHA', 'ZHB', 'ZKA', 'ZKB', 'ZLA', 'ZLB', 'ZMA', 'ZMB',
    'ZNA', 'ZNB', 'ZOA', 'ZOB', 'ZOLS', 'ZOLT', 'ZQA', 'ZQB', 'ZRA', 'ZRB',
    'ZRD', 'ZRU', 'ZTA', 'ZTB', 'ZUA', 'ZUB', 'ZXA', 'ZXB', 'ZXD', 'ZXU',
    'ZZA', 'ZZB', 'ZaA', 'ZaB', 'ZaD', 'ZaU', 'ZdA', 'ZdB', 'ZdD', 'ZdU',
    'ZeA', 'ZeB', 'ZfA', 'ZfB', 'ZgA', 'ZgB', 'ZhA', 'ZhB', 'ZkA', 'ZkB',
    'ZlA', 'ZlB', 'ZmA', 'ZmB', 'ZnA', 'ZnB', 'ZoA', 'ZoB', 'ZqA', 'ZqB',
    'ZrA', 'ZrB', 'ZrD', 'ZrU', 'ZtA', 'ZtB', 'ZuA', 'ZuB', 'ZxA', 'ZxB',
    'ZxD', 'ZxU', 'ZzA', 'ZzB', '0AE', '2AE', '4AE', 'YGa', '0AF', '2AF',
    '4AF', 'YAF', '0dR', '3dR', '4dR', 'WdR')

# AMBER_SUPPORTED_RESNAMES = set(RESPROT + RESNA + RESSOLV + RESSUGAR)
AMBER_SUPPORTED_RESNAMES = set(RESPROT + RESNA + RESSOLV)
