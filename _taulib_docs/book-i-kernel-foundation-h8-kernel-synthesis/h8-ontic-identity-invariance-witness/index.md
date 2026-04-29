---
{
  "projection_kind": "taulib_declaration",
  "title": "h8_ontic_identity_invariance_witness",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/h8-ontic-identity-invariance-witness/",
  "summary_short": "`def` declaration in `TauLib.BookI.KernelFoundation.H8KernelSynthesis`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.H8KernelSynthesis::h8_ontic_identity_invariance_witness",
  "declaration_slug": "h8-ontic-identity-invariance-witness",
  "kind": "def",
  "name": "h8_ontic_identity_invariance_witness",
  "module_name": "TauLib.BookI.KernelFoundation.H8KernelSynthesis",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/",
  "source_line_start": 126,
  "source_line_end": 127,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L126-L127",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.H8KernelSynthesis",
        "url": "/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L126-L127",
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

- Module: [TauLib.BookI.KernelFoundation.H8KernelSynthesis](/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/)
- Source path: [`TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L126-L127)
- Source range: L126-L127
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem `main-ontic-identity` (= I.T46)**: τ-kernel's
    normalisation map is unique, path-independent; no shadow
    identities; identity invariant under admissible symmetries;
    slippage = zero.

    Direct cite of `Tau.MetaLogic.ontic_identity_invariance`. -/
```

## Source Excerpt

```lean
def h8_ontic_identity_invariance_witness :
    OnticIdentityInvariance := ontic_identity_invariance
```
