---
{
  "projection_kind": "taulib_declaration",
  "title": "piApproxAt",
  "permalink": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/pi-approx-at/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.CouplingIdentityApproximants`.",
  "declaration_id": "TauLib.BookI.Boundary.CouplingIdentityApproximants::piApproxAt",
  "declaration_slug": "pi-approx-at",
  "kind": "def",
  "name": "piApproxAt",
  "module_name": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
  "module_url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/",
  "source_line_start": 127,
  "source_line_end": 127,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L127-L127",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L127-L127",
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
- Source path: [`TauLib/BookI/Boundary/CouplingIdentityApproximants.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L127-L127)
- Source range: L127-L127
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §6.1 `GerPi^(n)`**: the π-approximant at depth `n`,
    realised as the partial sum of the Madhava-type series from
    Wave 3c. -/
```

## Source Excerpt

```lean
def piApproxAt (n : Nat) : TauRat := TauReal.pi.approx n
```
