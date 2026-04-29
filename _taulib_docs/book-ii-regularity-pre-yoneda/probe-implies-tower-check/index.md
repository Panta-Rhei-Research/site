---
{
  "projection_kind": "taulib_declaration",
  "title": "probe_implies_tower_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/probe-implies-tower-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.PreYoneda`.",
  "declaration_id": "TauLib.BookII.Regularity.PreYoneda::probe_implies_tower_check",
  "declaration_slug": "probe-implies-tower-check",
  "kind": "def",
  "name": "probe_implies_tower_check",
  "module_name": "TauLib.BookII.Regularity.PreYoneda",
  "module_url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/",
  "source_line_start": 240,
  "source_line_end": 252,
  "registry_ids": [
    "II.R12"
  ],
  "related_registry_items": [
    {
      "id": "II.R12",
      "title": "Probe Naturality Equals Holomorphy",
      "url": "/registry/object/II.R12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L240-L252",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PreYoneda",
        "url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L240-L252",
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

- Module: [TauLib.BookII.Regularity.PreYoneda](/verify/taulib/docs/book-ii-regularity-pre-yoneda/)
- Source path: [`TauLib/BookII/Regularity/PreYoneda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L240-L252)
- Source range: L240-L252
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.R12` — Probe Naturality Equals Holomorphy

## Immediate Comment / Docstring

```lean
/-- [II.R12] Probe naturality implies tower coherence:
    if a function is natural with respect to ALL cylinder probes,
    then it is tower-coherent. This is verified by checking that
    naturality at every probe (k, pi_idx) implies the reduction
    compatibility condition. -/
```

## Source Excerpt

```lean
def probe_implies_tower_check (bound db : TauIdx) : Bool :=
  go 2 1 (bound * db + bound + db + 1)
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      -- Tower coherence: reduce(reduce(x, k+1), k) = reduce(x, k)
      -- This is what probe naturality reduces to
      let tc_ok := reduce (reduce x (k + 1)) k == reduce x k
      tc_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
