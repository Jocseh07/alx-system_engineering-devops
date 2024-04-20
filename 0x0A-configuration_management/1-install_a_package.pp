#!/usr/bin/pup
# install flask version 2.1.0
package {'flask':
  ensure   => '2.1.0.0',
  provider => 'pip3'
}
