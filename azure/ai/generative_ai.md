Generative AI
---

## Responsible Generative AI

- The Microsoft guidance for responsible generative AI is designed to be practical and actionable.
- It defines a `four stage process` to develop and implement a plan for responsible AI when using generative models.

### Identify potential harms that are relevant to your planned solution.

#### Identify potential harms
#### Prioritize identified harms
#### Test and verify the prioritized harms
#### Document and share the verified harms

### Measure the presence of these harms in the outputs generated by your solution.

### Mitigate the harms

- at multiple layers in your solution to minimize their presence and impact, and ensure transparent communication about potential risks to users.
- Mitigation of potential harms in a generative AI solution involves a layered approach, in which mitigation techniques can be applied at each of four layers:
    - Model
    - Safety System
    - Metaprompt and grounding
    - User experience

### Operate the solution responsibly

- by defining and following a deployment and operational readiness plan.
- Considerations that help you ensure a successful release and subsequent operations:

#### Complete prerelease reviews

- Before releasing a generative AI solution, `identify the various compliance requirements` in your organization and industry and ensure the appropriate teams are given the opportunity to review the system and its documentation.
- Common compliance reviews include:
    - Legal
    - Privacy
    - Security
    - Accessibility

#### Release and operate the solution

- A successful release requires some planning and preparation.
- Consider the following guidelines:
    - `Devise a phased delivery plan` that enables you to release the solution initially to restricted group of users. This approach enables you to gather feedback and identify problems before releasing to a wider audience.
    - `Create an incident response plan` that includes estimates of the time taken to respond to unanticipated incidents.
    - `Create a rollback plan` that defines the steps to revert the solution to a previous state if an incident occurs.
    - `Implement the capability to immediately block harmful system responses` when they're discovered.
    - `Implement a capability to block specific users, applications, or client IP addresses` in the event of system misuse.
    - `Implement a way for users to provide feedback and report issues`. In particular, enable users to report generated content as "inaccurate", "incomplete", "harmful", "offensive", or otherwise problematic.
    - `Track telemetry data that enables you` to determine user satisfaction and identify functional gaps or usability challenges. Telemetry collected should comply with privacy laws and your own organization's policies and commitments to user privacy.

#### Utilize Azure AI Content Safety

- Several Azure AI resources provide built-in analysis of the content they work with, including Language, Vision, and Azure OpenAI by using `content filters`.
- It provides more features focusing on keeping AI and copilots safe from risk.
- These features include detecting inappropriate or offensive language, both from input or generated, and detecting risky or inappropriate inputs.
- Features in Azure AI Content Safety include:
    - Prompt Shields
    - Groundness Detection
    - Protected material detection
    - Custom categories
