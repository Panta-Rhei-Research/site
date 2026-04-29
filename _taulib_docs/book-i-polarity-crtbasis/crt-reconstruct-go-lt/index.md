---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_reconstruct_go_lt",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/crt-reconstruct-go-lt/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::crt_reconstruct_go_lt",
  "declaration_slug": "crt-reconstruct-go-lt",
  "kind": "theorem",
  "name": "crt_reconstruct_go_lt",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 314,
  "source_line_end": 327,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L314-L327",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.CRTBasis",
        "url": "/verify/taulib/docs/book-i-polarity-crtbasis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L314-L327",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Polarity.CRTBasis](/verify/taulib/docs/book-i-polarity-crtbasis/)
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L314-L327)
- Source range: L314-L327
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- crt_reconstruct_go result < primorial k when acc < primorial k. -/
```

## Source Excerpt

```lean
private theorem crt_reconstruct_go_lt (residues : List TauIdx) (k : TauIdx)
    (hk : primorial k > 0) :
    ∀ (i fuel : Nat) (acc : TauIdx), acc < primorial k →
    crt_reconstruct_go residues k i fuel acc < primorial k := by
  intro i fuel
  induction fuel generalizing i with
  | zero => intro acc hacc; unfold crt_reconstruct_go; simp; exact hacc
  | succ n ih =>
    intro acc hacc
    unfold crt_reconstruct_go
    simp only [Nat.succ_ne_zero, ↓reduceIte]
    split
    · exact hacc
    · exact ih (i + 1) _ (Nat.mod_lt _ hk)
```
