---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRealQ.one",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/one-l175/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Bridge.TauRealQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRealQuotient::TauRealQ.one",
  "declaration_slug": "one-l175",
  "kind": "def",
  "name": "TauRealQ.one",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/",
  "source_line_start": 175,
  "source_line_end": 192,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L175-L192",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRealQuotient",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L175-L192",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRealQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L175-L192)
- Source range: L175-L192
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
def TauRealQ.one  : TauRealQ := CauchyTauReal.one.toQ

@[simp] theorem TauRealQ.add_mk (a b : CauchyTauReal) :
    TauRealQ.add a.toQ b.toQ = (a.add b).toQ := rfl
@[simp] theorem TauRealQ.mul_mk (a b : CauchyTauReal) :
    TauRealQ.mul a.toQ b.toQ = (a.mul b).toQ := rfl
@[simp] theorem TauRealQ.neg_mk (a : CauchyTauReal) :
    TauRealQ.neg a.toQ = a.neg.toQ := rfl

-- ============================================================
-- PART 5: Bare typeclass instances
-- ============================================================

instance : Zero TauRealQ := ⟨TauRealQ.zero⟩
instance : One  TauRealQ := ⟨TauRealQ.one⟩
instance : Add  TauRealQ := ⟨TauRealQ.add⟩
instance : Mul  TauRealQ := ⟨TauRealQ.mul⟩
instance : Neg  TauRealQ := ⟨TauRealQ.neg⟩
```
