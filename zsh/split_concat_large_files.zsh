cd#!/usr/bin/zsh

QUALIFYING_FILE_SIZE=20_000 # bytes
CHUNK_SIZE=1
PATH_TO_ITERATE=~/XSDCard/Misc

case $1 in
  "split")
    for file in $PATH_TO_ITERATE/**/*(.); do
      if [[ $(stat -c %s "$file") -gt $QUALIFYING_FILE_SIZE ]]; then
          split --verbose $file "$file.part~"
          rm "$file"
      fi
    done
  ;;

  "reassemble")
    for file in $PATH_TO_ITERATE/**/*(.); do
      if [[ $file == *.part~aa ]]; then
          cat ${file//'~aa'/'~'}* > ${file//'.part~aa'/''}
          rm ${file//'~aa'/'~'}*
      fi
    done
  ;;

  *)
    echo "Invalid option"
  ;;
esac