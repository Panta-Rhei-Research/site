---
{
  "projection_kind": "taulib_declaration",
  "title": "code_decode_uniqueness_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/code-decode-uniqueness-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.HartogsExtension`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.HartogsExtension::code_decode_uniqueness_check",
  "declaration_slug": "code-decode-uniqueness-check",
  "kind": "def",
  "name": "code_decode_uniqueness_check",
  "module_name": "TauLib.BookII.CentralTheorem.HartogsExtension",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/",
  "source_line_start": 221,
  "source_line_end": 236,
  "registry_ids": [
    "II.T37"
  ],
  "related_registry_items": [
    {
      "id": "II.T37",
      "title": "Hartogs Extension Uniqueness",
      "url": "/registry/object/II.T37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L221-L236",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.HartogsExtension",
        "url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L221-L236",
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

- Module: [TauLib.BookII.CentralTheorem.HartogsExtension](/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/)
- Source path: [`TauLib/BookII/CentralTheorem/HartogsExtension.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L221-L236)
- Source range: L221-L236
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T37` — Hartogs Extension Uniqueness

## Immediate Comment / Docstring

```lean
/-- [II.T37] Code/Decode witness for uniqueness: the Code/Decode bijection
    (II.T35) ensures that a function on Z/P_kZ is uniquely determined by
    its values. Combined with BndLift tower coherence, this means the
    Hartogs extension is unique.

    We verify: code_extract(bndlift_fn, k, x) = reduce(x, k) for
    the bndlift "function" at stage k. -/
```

## Source Excerpt

```lean
def code_decode_uniqueness_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      -- The bndlift "function" at stage k
      let bndlift_fn : TauIdx -> Int := fun n => (bndlift n k : Int)
      -- code_extract should give bndlift(reduce(x, k+1), k) = reduce(reduce(x, k+1), k+1)
      -- = reduce(x, k+1) = bndlift(x, k) for x < P_{k+1}
      let coded := code_extract bndlift_fn (k + 1) x
      let direct := (bndlift (reduce x (k + 1)) k : Int)
      (coded == direct) && go x (k + 1) (fuel - 1)
  termination_by fuel
```
