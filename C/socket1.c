#include <stdio.h>
#include <sys/socket.h>

/* 
Socket analogous to installing a telephone
    * socket() creates a socket is equivalent to installing a telephone.
    * Communication is analogous to telephone calls
    * One app calls bind() to bind the socket to a well-known address, then calls listen() to notify the kernel of willingness to accept incoming connections. This is like having a telephone num in mind and ensuring that our tel is turned on so that people can call us
    * Other apps establishes connection by calling connect(), specifying the address of the socket to which the connection is ot be made (dialing someone phone number)
    * The application that called listen() then accepts the connection using accept(). This is like picking the telephone when it rings 
    * Once connection is established, data can be transmitted in both directions between applications until one of them close the string down using close(). Communication is done using the traditional read() and write() system calls or via a number of specific system calls (such as send() or recv()) that provide additional functionality.
*/


void main()
{
    // int socket(int domain, int type, int protocol);
        // domain: specifies communication domain for the socket
        // type: specifies the socket type (SOCK_STREAM, SOCK_DRAM)
        // protocol: 0 in our case

    // int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
        // sockfd: file descriptor obtained from a previous call to socket()
        // addr: pointer to a structure specifying the address to whic this socket is to be bound 
}