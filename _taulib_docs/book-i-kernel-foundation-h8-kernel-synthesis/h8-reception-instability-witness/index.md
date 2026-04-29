---
{
  "projection_kind": "taulib_declaration",
  "title": "h8_reception_instability_witness",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/h8-reception-instability-witness/",
  "summary_short": "`def` declaration in `TauLib.BookI.KernelFoundation.H8KernelSynthesis`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.H8KernelSynthesis::h8_reception_instability_witness",
  "declaration_slug": "h8-reception-instability-witness",
  "kind": "def",
  "name": "h8_reception_instability_witness",
  "module_name": "TauLib.BookI.KernelFoundation.H8KernelSynthesis",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-h8-kernel-synthesis/",
  "source_line_start": 165,
  "source_line_end": 166,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L165-L166",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L165-L166",
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
- Source path: [`TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/H8KernelSynthesis.lean#L165-L166)
- Source range: L165-L166
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem `main-reception` (= I.T48)**: no identity-faithful
    functor τ → diagonal-resonant-host system can preserve
    distinctness, identity, and isomorphism reflection
    simultaneously.

    Concrete witness: every orthodox foundation (ZFC, CIC, HoTT)
    exhibits structural instability when receiving τ
    (`orthodox_instability`). -/
```

## Source Excerpt

```lean
def h8_reception_instability_witness (f : OrthodoxFoundation) :
    StructuralInstability := orthodox_instability f
```
