---
{
  "projection_kind": "taulib_declaration",
  "title": "BPolarized",
  "permalink": "/verify/taulib/docs/book-i-polarity-polarized-germs/bpolarized/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.PolarizedGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.PolarizedGerms::BPolarized",
  "declaration_slug": "bpolarized",
  "kind": "def",
  "name": "BPolarized",
  "module_name": "TauLib.BookI.Polarity.PolarizedGerms",
  "module_url": "/verify/taulib/docs/book-i-polarity-polarized-germs/",
  "source_line_start": 96,
  "source_line_end": 97,
  "registry_ids": [
    "I.D26"
  ],
  "related_registry_items": [
    {
      "id": "I.D26",
      "title": "Polarized Omega-Germ",
      "url": "/registry/object/I.D26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L96-L97",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PolarizedGerms",
        "url": "/verify/taulib/docs/book-i-polarity-polarized-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L96-L97",
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

- Module: [TauLib.BookI.Polarity.PolarizedGerms](/verify/taulib/docs/book-i-polarity-polarized-germs/)
- Source path: [`TauLib/BookI/Polarity/PolarizedGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L96-L97)
- Source range: L96-L97
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D26` — Polarized Omega-Germ

## Immediate Comment / Docstring

```lean
/-- [I.D26] B-polarized at a prime p: C-channel eventually freezes AND B-channel
    keeps refining (cofinal). Ground truth (chunk_0123, lines 369-386):
    ∂τ₃^B := { [x•] | ∃N ∀n≥N, Cₙ=α₁  ∧  ∀M ∃n≥M, Bₙ≠α₁ }. -/
```

## Source Excerpt

```lean
def BPolarized (p : TauIdx) : Prop :=
  eventually_constant (c_channel_seq p) ∧ cofinal (b_channel_seq p)
```
