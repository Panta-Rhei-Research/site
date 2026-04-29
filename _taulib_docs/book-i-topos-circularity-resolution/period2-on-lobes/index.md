---
{
  "projection_kind": "taulib_declaration",
  "title": "Period2OnLobes",
  "permalink": "/verify/taulib/docs/book-i-topos-circularity-resolution/period2-on-lobes/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.CircularityResolution`.",
  "declaration_id": "TauLib.BookI.Topos.CircularityResolution::Period2OnLobes",
  "declaration_slug": "period2-on-lobes",
  "kind": "def",
  "name": "Period2OnLobes",
  "module_name": "TauLib.BookI.Topos.CircularityResolution",
  "module_url": "/verify/taulib/docs/book-i-topos-circularity-resolution/",
  "source_line_start": 161,
  "source_line_end": 164,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L161-L164",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.CircularityResolution",
        "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L161-L164",
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

- Module: [TauLib.BookI.Topos.CircularityResolution](/verify/taulib/docs/book-i-topos-circularity-resolution/)
- Source path: [`TauLib/BookI/Topos/CircularityResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L161-L164)
- Source range: L161-L164
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Period-2 oscillation between the two lobe atoms**: case (c).
    After some index `n0`, the iteration alternates between `T` and
    `F`.  This is the structural shape that gives the Liar its
    `Both = e_+ + e_-` ω-germ stabilised value. -/
```

## Source Excerpt

```lean
def Period2OnLobes (Φ : Truth4 → Truth4) (s : Truth4) : Prop :=
  ∃ n0 : Nat, ∀ n, n0 ≤ n →
    (cauchyIter Φ n s = T ∧ cauchyIter Φ (n + 1) s = F) ∨
    (cauchyIter Φ n s = F ∧ cauchyIter Φ (n + 1) s = T)
```
