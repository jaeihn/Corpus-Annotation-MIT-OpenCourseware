require "csv"
require "AnyStyle"

counter = 0 
path_processed = "./processed/"
path_parsed = "./parsed/"
malformed_count = 0
prev_author = ""

Dir.each_child(path_processed) {|folder| 
    if File.directory?(path_processed + folder)
        Dir.each_child(path_processed + folder) { |file|
            if file != ".DS_Store"
                begin 
                    annotations = CSV.read(path_processed + folder +'/' + file,  col_sep: "\t", headers: false )
                    File.open(path_parsed + folder +"/" + file, "w") do |f|
                        for category, reading in annotations
                            f.write("#{category}\t")
                            if reading != nil
                                parsed_reading = AnyStyle.parse(reading)[0]
                                if parsed_reading.key?(:author) 
                                    if parsed_reading[:author] == [{:literal=>"."}]
                                        f.write("#{prev_author}\t")
                                    else
                                        f.write("#{parsed_reading[:author]}\t")
                                        prev_author = parsed_reading[:author]
                                    end
                                else
                                    f.write("\t")
                                end
                                f.write("#{parsed_reading[:title]}\t")
                                f.write("#{parsed_reading[:type]}\t")
                                f.write("#{parsed_reading[:'container-title']}\t")
                                f.write("#{parsed_reading[:date]}")
                                f.write("\n")
                            end
                        end
                    end
                rescue CSV::MalformedCSVError
                    malformed_count += 1
                    next
                end
                counter += 1
                if counter % 100 == 0
                    p "#{counter} ..."
                end
            end
        }
    end
}

p malformed_count
p "END"









# require "csv"
# require "AnyStyle"

# counter = 0 
# path_processed = "./processed/"
# path_parsed = "./parsed/"
# malformed_count = 0
# prev_author = ""

# Dir.each_child(path_processed) {|folder| 
#     if File.directory?(path_processed + folder)
#         Dir.each_child(path_processed + folder) { |file|
#             if file != ".DS_Store"
#                 begin 
#                     annotations = CSV.read(path_processed + folder +'/' + file, encoding: 'iso-8859-1:utf-8', col_sep: "\t", headers: false )
#                     File.open(path_parsed + folder +"/" + file, "w") do |f|
#                         for category, reading in annotations
#                             f.write("#{category}\t")
#                             if reading != ""
#                                 parsed_reading = AnyStyle.parse(reading)[0]
#                                 if parsed_reading.key?(:author) 
#                                     parsed_reading[:author] == [{:literal=>"."}]
#                                     f.write("#{prev_author}\t")
#                                 else
#                                     f.write("#{parsed_reading[:author]}\t")
#                                     prev_author = parsed_reading[:author]
#                                 end
#                                 f.write("#{parsed_reading[:title][0]}\t")
#                                 f.write("#{parsed_reading[:type]}\t")
#                                 f.write("#{parsed_reading[:'container-title'][0]}\t")
#                                 f.write("#{parsed_reading[:date][0]}")
#                                 f.write("\n")
#                             end
#                             counter += 1
#                             if counter == 10
#                                 break
#                             end
#                         end
#                     end
#                 rescue CSV::MalformedCSVError
#                     malformed_count += 1
#                     next
#                 end
#             end
#         }
#     end
# }

# p malformed_count
# p "END"

