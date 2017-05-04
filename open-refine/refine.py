import os.path, time, json
import pandas
import sys
import webbrowser
import requests
import six
from six.moves import html_parser
from six.moves import urllib
import tempfile

class Refine:
  def __init__(self, df, server='http://127.0.0.1:3333', options=None):
    self.server = server[0,-1] if server.endswith('/') else server
    #write the pandas frame to csv file
    #create temp file
    __, file_name = tempfile.mkstemp()
    outfile = os.fdopen(__, 'r+')
    df.to_csv(outfile)
    outfile.close()
    file_path = file_name
    project_name = options['project_name'] if options != None and 'project_name' in options else file_name


    values = {
      'project-name' : project_name
    }
    outfile = open(file_path, 'r+')
    files = {'file': outfile}
    url = self.server + '/command/core/create-project-from-upload'
    response = requests.post(url, files=files, data=values)
    url_params = urllib.parse.parse_qs(urllib.parse.urlparse(response.url).query)
    outfile.close()
    os.remove(file_name)
    if 'project' in url_params:
      self.id = id = url_params['project'][0]
      self.project_name = project_name
      #open the project in the webbrowser.
      webbrowser.open('http://127.0.0.1:3333/project?project=' + id, new=1)
  
  
  def export_pandas_frame(self, format='tsv'):
    """
    Export the data from openrefine and transfer it to pandas frame
    Returns: 
      The new pandas frame with the data changed by the GUI operation  
    """
    values = {
      'engine' : '{"facets":[],"mode":"row-based"}',
      'project' : self.id,
      'format' : format
    }
    response = requests.post(self.server + '/command/core/export-rows/' + self.project_name + '.' + format, data = values)
    st = six.StringIO(response.content.decode('utf-8'))
    df = pandas.read_csv(st, sep="\t")
    self.delete_project()
    return df
    
  def delete_project(self):
    """
    Delete the openrefine project
    """
    values = {
      'project' : self.id
    }
    response = requests.post(self.server + '/command/core/delete-project', data=values)
    response_json = json.loads(response.content.decode('utf-8'))
    return 'code' in response_json and response_json['code'] == 'ok'
