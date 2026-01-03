# ZTNA
Zero Trust Network Access (ZTNA) is a security model based on the principle “never trust, always verify.” Unlike traditional perimeter-based security, ZTNA assumes that no user, device, or application is trusted by default, whether inside or outside the network.

ZTNA provides secure, identity- and context-based access to applications instead of granting broad network access. Users connect only to specific applications they are authorized to use, not to the entire network.

#How ZTNA Works (Flow)
User requests access to an application
ZTNA controller authenticates the user (MFA, IAM)
Device security posture is verified
Policy engine evaluates access rules
Secure, encrypted connection is established only to the requested app
