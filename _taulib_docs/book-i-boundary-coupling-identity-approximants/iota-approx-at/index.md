---
{
  "projection_kind": "taulib_declaration",
  "title": "iotaApproxAt",
  "permalink": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/iota-approx-at/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.CouplingIdentityApproximants`.",
  "declaration_id": "TauLib.BookI.Boundary.CouplingIdentityApproximants::iotaApproxAt",
  "declaration_slug": "iota-approx-at",
  "kind": "def",
  "name": "iotaApproxAt",
  "module_name": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
  "module_url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/",
  "source_line_start": 136,
  "source_line_end": 136,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L136-L136",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
        "url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L136-L136",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Boundary.CouplingIdentityApproximants](/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/)
- Source path: [`TauLib/BookI/Boundary/CouplingIdentityApproximants.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L136-L136)
- Source range: L136-L136
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §6.1 `GerIota^(n)`**: the ι_τ-approximant at depth `n`,
    realised via Wave 4's operational `TauReal.iota_tau = 2/(π+e)`
    evaluated at depth `n`. -/
```

## Source Excerpt

```lean
def iotaApproxAt (n : Nat) : TauRat := TauReal.iota_tau.approx n
```
