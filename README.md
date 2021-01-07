# Fdfs_client py

The Python interface to the Fastdfs Ver 4.06.

## Installation

    $ sudo python setup.py install

## Getting Started
	1. import fdfs_client.client module
	2. instantiate class Fdfs_client
	3. call memeber functions

    >>> from fdfs_client.client import *
    >>> from fdfs_client.file_crypt import FileCrypt
    >>> fc = FileCrypt()
    >>> client = Fdfs_client(get_tracker_conf('fdfs_config.conf'))
    >>> ret = client.upload_by_filename('test', file_crypt=fc)
	>>> ret
	{'Group name':'group1','Status':'Upload successed.', 'Remote file_id':'group1/M00/00/00/
    	wKjzh0_xaR63RExnAAAaDqbNk5E1398.py','Uploaded size':'6.0KB','Local file name':'test'
		, 'Storage IP':'192.168.243.133'}
    >>> ret2 = client.download_to_file('2.docx', res['Remote file_id'], file_crypt=fc)
## API Reference

Class Fdfs_client:

member functions:

* upload_by_filename(self, filename, meta_dict = None)
  '''
  Upload a file to Storage server.
  arguments:
        @filename: string, name of file that will be uploaded
        @meta_dict: dictionary e.g.:{
            'ext_name'  : 'jpg',
            'file_size' : '10240B',
            'width'     : '160px',
            'hight'     : '80px'
        } meta_dict can be null
        @return dict {
            'Group name'      : group_name,
            'Remote file_id'  : remote_file_id,
            'Status'          : 'Upload successed.',
            'Local file name' : local_file_name,
            'Uploaded size'   : upload_size,
            'Storage IP'      : storage_ip
        } if success else None

* upload_by_buffer(self, filebuffer, file_ext_name = None, meta_dict = None)
  '''
  Upload a buffer to Storage server.
  arguments:
        @filebuffer: string, buffer
        @file_ext_name: string, file extend name
        @meta_dict: dictionary e.g.:{
            'ext_name'  : 'jpg',
            'file_size' : '10240B',
            'width'     : '160px',
            'hight'     : '80px'
        }
        @return dict {
            'Group name'      : group_name,
            'Remote file_id'  : remote_file_id,
            'Status'          : 'Upload successed.',
            'Local file name' : '',
            'Uploaded size'   : upload_size,
            'Storage IP'      : storage_ip
        }
  '''

* upload_slave_by_filename(self, filename, remote_file_id, prefix_name, \
                                 meta_dict = None)
  '''
  Upload slave file to Storage server.
  arguments:
       @filename: string, local file name
       @remote_file_id: string, remote file id
       @prefix_name: string
       @meta_dict: dictionary e.g.:{
           'ext_name'  : 'jpg',
           'file_size' : '10240B',
           'width'     : '160px',
           'hight'     : '80px'
       }
       @return dictionary {
           'Status'        : 'Upload slave successed.',
           'Local file name' : local_filename,
           'Uploaded size'   : upload_size,
           'Remote file id'  : remote_file_id,
           'Storage IP'      : storage_ip
       }
  '''

* upload_slave_by_buffer(self, filebuffer, remote_file_id, \
                               meta_dict = None, file_ext_name = None)
  '''
  Upload slave file by buffer
  arguments:
       @filebuffer: string
       @remote_file_id: string
       @meta_dict: dictionary e.g.:{
           'ext_name'  : 'jpg',
           'file_size' : '10240B',
           'width'     : '160px',
           'hight'     : '80px'
       }
       @return dictionary {
           'Status'        : 'Upload slave successed.',
           'Local file name' : local_filename,
           'Uploaded size'   : upload_size,
           'Remote file id'  : remote_file_id,
           'Storage IP'      : storage_ip
       }
  '''

* upload_appender_by_filename(self, local_filename, meta_dict = None)
  '''
  Upload an appender file by filename.
  arguments:
       @local_filename: string
       @meta_dict: dictionary e.g.:{
           'ext_name'  : 'jpg',
           'file_size' : '10240B',
           'width'     : '160px',
           'hight'     : '80px'
       }    Notice: it can be null
       @return dict {
           'Group name'      : group_name,
           'Remote file_id'  : remote_file_id,
           'Status'          : 'Upload successed.',
           'Local file name' : '',
           'Uploaded size'   : upload_size,
           'Storage IP'      : storage_ip
	   }
  '''

* upload_appender_by_buffer(self, filebuffer, file_ext_name = None, meta_dict = None)
  '''
  Upload a buffer to Storage server.
  arguments:
       @filebuffer: string
       @file_ext_name: string, can be null
       @meta_dict: dictionary, can be null
       @return dict {
           'Group name'      : group_name,
           'Remote file_id'  : remote_file_id,
           'Status'          : 'Upload successed.',
           'Local file name' : '',
           'Uploaded size'   : upload_size,
           'Storage IP'      : storage_ip
       }
  '''

* delete_file(self, remote_file_id)
  '''
  Delete a file from Storage server.
  arguments:
       @remote_file_id: string, file_id of file that is on storage server
       @return tuple ('Delete file successed.', remote_file_id, storage_ip)
  '''

* download_to_file(self, local_filename, remote_file_id, offset = 0, down_bytes = 0)
  '''
  Download a file from Storage server.
  arguments:
       @local_filename: string, local name of file
       @remote_file_id: string, file_id of file that is on storage server
	   @offset: long
	   @down_bytes: long
       @return dict {
           'Remote file_id'  : remote_file_id,
           'Content'         : local_filename,
           'Download size'   : downloaded_size,
           'Storage IP'      : storage_ip
       }
  '''

* download_to_buffer(self, remote_file_id, offset = 0, down_bytes = 0)
  '''
  Download a file from Storage server and store in buffer.
  arguments:
	   @remote_file_id: string, file_id of file that is on storage server
  	   @offset: long
	   @down_bytes: long
       @return dict {
           'Remote file_id'  : remote_file_id,
           'Content'         : file_buffer,
           'Download size'   : downloaded_size,
           'Storage IP'      : storage_ip
       }
  '''

* list_one_group(self, group_name)
  '''
  List one group information.
  arguments:
       @group_name: string, group name will be list
       @return Group_info,  instance
  '''

* list_all_groups(self)
  '''
  List all group information.
       @return dictionary {
           'Groups count' : group_count,
           'Groups'       : list of groups
       }
  '''

* list_servers(self, group_name, storage_ip = None)
  '''
  List all storage servers information in a group
  arguments:
       @group_name: string
       @return dictionary {
           'Group name' : group_name,
           'Servers'    : server list,
       }
  '''

* get_meta_data(self, remote_file_id)
  '''
  Get meta data of remote file.
  arguments:
       @remote_fileid: string, remote file id
       @return dictionary, meta data
  '''

* set_meta_data(self, remote_file_id, \
                      meta_dict, op_flag = STORAGE_SET_METADATA_FLAG_OVERWRITE)
  '''
  Set meta data of remote file.
  arguments:
       @remote_file_id: string
       @meta_dict: dictionary
       @op_flag: char, 'O' for overwrite, 'M' for merge
       @return dictionary {
           'Status'     : status,
           'Storage IP' : storage_ip
       }
  '''

* append_by_filename(self, local_filename, remote_fileid)
  '''
  Append a file of Storage server
  arguments:
       @local_filename: string
  	   @remote_fileid: string
       @return dict {
           'Group name'      : group_name,
           'Remote file_id'  : remote_file_id,
           'Status'          : 'Upload successed.',
           'Local file name' : '',
           'Uploaded size'   : upload_size,
           'Storage IP'      : storage_ip
       }
  '''

* append_by_buffer(self, file_buffer, remote_fileid)
  '''
  Append a file of Storage server
  arguments:
       @file_buffer: string
  	   @remote_fileid: string
       @return dict {
           'Group name'      : group_name,
           'Remote file_id'  : remote_file_id,
           'Status'          : 'Upload successed.',
           'Local file name' : '',
           'Uploaded size'   : upload_size,
           'Storage IP'      : storage_ip
       }
  '''

* truncate_file(self, truncated_filesize, appender_fileid)
  '''
  Truncate file in Storage server.
  arguments:
       @truncated_filesize: long
       @appender_fileid: remote_fileid
       @return: dictionary {
           'Status'     : 'Truncate successed.',
           'Storage IP' : storage_ip
       }
  '''

* modify_by_filename(self, filename, appender_fileid, offset = 0)
  '''
  Modify a file in Storage server by filename.
  arguments:
       @filename: string, local file name
       @offset: long, file offset
       @appender_fileid: string, remote file id
       @return: dictionary {
           'Status'     : 'Modify successed.',
           'Storage IP' : storage_ip
       }
  '''

* modify_by_buffer(self, filebuffer, appender_fileid, offset = 0)
  '''
  Modify a file in Storage server by buffer.
  arguments:
       @filebuffer: string, file buffer
       @offset: long, file offset
       @appender_fileid: string, remote file id
       @return: dictionary {
           'Status'     : 'Modify successed.',
           'Storage IP' : storage_ip
       }
  '''

### Connection Pools

Behind the scenes, fdfs_client-py uses a connection pool to manage connections to
sets of tracker server and storage server.


## Versioning scheme

fdfs_client-py ver 1.2.7b support client protol of Fastdfs ver 4.06.
Python must be ver 2.6 later.

Author
------

fdfs_client-py is developed and maintained by scott yuan (scottzer8@gmail.com)

fdfs_client-py is bug fixed and maintained by hay86

It can be found here: http://github.com/hay86/fdfs_client-py

Special thanks to:

* Andy Mccurdy, author of redis-py, referenced his code.
* g.rodola, author sendfile module for python, g.rodola@gmail.com
