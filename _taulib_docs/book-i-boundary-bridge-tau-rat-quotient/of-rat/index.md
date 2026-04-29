---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRatQ.ofRat",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/of-rat/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Bridge.TauRatQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRatQuotient::TauRatQ.ofRat",
  "declaration_slug": "of-rat",
  "kind": "def",
  "name": "TauRatQ.ofRat",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/",
  "source_line_start": 381,
  "source_line_end": 382,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L381-L382",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L381-L382",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRatQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L381-L382)
- Source range: L381-L382
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Embed `Rat` into `TauRatQ`: `q ↦ ⟨⟨q.num.toNat, (-q.num).toNat⟩, q.den, _⟩.toQ`.

    Unconditional pattern: works regardless of sign of `q.num`. When
    `q.num ≥ 0`, `q.num.toNat = q.num` and `(-q.num).toNat = 0`; when
    `q.num < 0`, `q.num.toNat = 0` and `(-q.num).toNat = -q.num`.
    Either way, `pos - neg = q.num` as `Int`. -/
```

## Source Excerpt

```lean
def TauRatQ.ofRat (q : Rat) : TauRatQ :=
  (⟨⟨q.num.toNat, (-q.num).toNat⟩, q.den, q.pos⟩ : TauRat).toQ
```
